export interface Env {
  EMAIL_API_KEY: string;
  EMAILS_SERVICE_URL: string;
  CONTACT_RECIPIENT: string;
  ALLOWED_ORIGIN: string;
  CONTACT_TENANT_ID: string;
}

export const MAX_FIELD_LENGTH = 5000;

export interface ContactConfig {
  serviceUrl: string;
  recipient: string;
  allowedOrigin: string;
  tenantId: string;
}

export function resolveConfig(env: Env): ContactConfig | null {
  const required = [env.EMAILS_SERVICE_URL, env.CONTACT_RECIPIENT, env.ALLOWED_ORIGIN, env.CONTACT_TENANT_ID];
  if (required.some((value) => !value)) {
    return null;
  }
  return {
    serviceUrl: env.EMAILS_SERVICE_URL.replace(/\/+$/, ""),
    recipient: env.CONTACT_RECIPIENT,
    allowedOrigin: env.ALLOWED_ORIGIN,
    tenantId: env.CONTACT_TENANT_ID,
  };
}
