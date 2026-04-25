const KLAVIYO_API_BASE = 'https://a.klaviyo.com/api';
const KLAVIYO_REVISION = '2026-04-15';

function json(statusCode, body) {
  return {
    statusCode,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'no-store',
    },
    body: JSON.stringify(body),
  };
}

function parseBody(rawBody) {
  if (!rawBody) return {};
  try {
    return JSON.parse(rawBody);
  } catch {
    return null;
  }
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

async function callKlaviyo(path, apiKey, payload) {
  const response = await fetch(`${KLAVIYO_API_BASE}${path}`, {
    method: 'POST',
    headers: {
      Authorization: `Klaviyo-API-Key ${apiKey}`,
      accept: 'application/json',
      'content-type': 'application/json',
      revision: KLAVIYO_REVISION,
    },
    body: JSON.stringify(payload),
  });

  const text = await response.text();
  let data = null;

  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      data = { raw: text };
    }
  }

  if (!response.ok) {
    const error = new Error(`Klaviyo request failed: ${response.status}`);
    error.status = response.status;
    error.details = data;
    throw error;
  }

  return data;
}

exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return json(405, { error: 'method_not_allowed' });
  }

  const apiKey = process.env.KLAVIYO_PRIVATE_API_KEY;
  const listId = process.env.KLAVIYO_ALPHA_LIST_ID;

  if (!apiKey || !listId) {
    return json(500, { error: 'missing_klaviyo_configuration' });
  }

  const body = parseBody(event.body);
  if (!body) {
    return json(400, { error: 'invalid_json' });
  }

  const email = String(body.email || '').trim().toLowerCase();
  const promoCodeUsed = String(body.promoCodeUsed || '').trim().toUpperCase();
  const marketingConsent = Boolean(body.marketingConsent);
  const consentedAt = body.consentedAt || new Date().toISOString();
  const market = String(body.market || 'KR').trim().toUpperCase();
  const locale = String(body.locale || 'ko-KR').trim();
  const sourcePath = String(body.sourcePath || '').trim();
  const referrer = String(body.referrer || '').trim();

  if (!email || !isValidEmail(email)) {
    return json(400, { error: 'invalid_email' });
  }

  try {
    await callKlaviyo('/profile-import', apiKey, {
      data: {
        type: 'profile',
        attributes: {
          email,
          properties: {
            alpha_pre_registered: true,
            alpha_market: market,
            alpha_locale: locale,
            alpha_source_path: sourcePath || null,
            alpha_referrer: referrer || null,
            alpha_promo_code_used: promoCodeUsed || null,
            alpha_marketing_consent: marketingConsent,
            alpha_registered_at: consentedAt,
          },
        },
      },
    });

    if (marketingConsent) {
      await callKlaviyo('/profile-subscription-bulk-create-jobs/', apiKey, {
        data: {
          type: 'profile-subscription-bulk-create-job',
          attributes: {
            custom_source: 'Lucive Alpha Landing',
            profiles: {
              data: [
                {
                  type: 'profile',
                  attributes: {
                    email,
                    subscriptions: {
                      email: {
                        marketing: {
                          consent: 'SUBSCRIBED',
                        },
                      },
                    },
                  },
                },
              ],
            },
          },
          relationships: {
            list: {
              data: {
                type: 'list',
                id: listId,
              },
            },
          },
        },
      });
    }

    return json(200, {
      ok: true,
      marketingConsent,
      email,
    });
  } catch (error) {
    console.error('pre-register klaviyo error', {
      status: error.status,
      details: error.details,
      message: error.message,
    });

    return json(502, {
      error: 'klaviyo_request_failed',
    });
  }
};
