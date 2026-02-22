# 260115 Security Audit — Conduit Monism

Date: 2026-01-15  
Scope: `website/` (Next.js frontend) + repo hygiene relevant to frontend deployment  
Auditor: automated + manual static review (local)

## Executive summary

Overall: **Low application risk in the frontend code** (no obvious XSS sinks, no storage of secrets, no network calls, no third‑party scripts observed), but **high operational risk** from local tooling configuration:

- **Critical**: A GitHub credential was used in a command line, which is retained in terminal history/logs.
- **High**: Node is running with TLS certificate verification disabled (`NODE_TLS_REJECT_UNAUTHORIZED=0`), which breaks HTTPS trust and makes dependency downloads and API calls vulnerable to MITM.

These two issues are outside the Next.js code, but they are the fastest way to lose the repo and/or ship compromised artefacts.

### Patch status (in-repo)

- **Implemented**: Global security headers + CSP via `website/next.config.ts`.
- **Implemented**: Refuse `npm run dev|build|start|lint` when `NODE_TLS_REJECT_UNAUTHORIZED=0` via `website/package.json` pre-scripts.
- **Not implementable from code**: Revoking/rotating the exposed GitHub credential and purging local history/logs remains an operational task.

## Method

- Static inspection of Next.js app router pages/components under `website/src/`
- Pattern scan for common secrets and unsafe browser sinks (XSS primitives, eval, storage, cookies)
- Dependency vulnerability audit using `npm audit` from `website/` (based on `package-lock.json`)

Limitations:
- The local `.env` and `.env.example` at repo root exist but were not readable in this environment (filtered by tooling ignore rules). Treat them as **potential secret carriers** until you confirm their contents locally.
- This audit does not include dynamic testing, SAST/DAST, or server/hosting configuration validation (Vercel/NGINX/Cloudflare).

## Findings

### 1) Critical — GitHub credential exposure via terminal history/logs (operational)

Evidence:
- Terminal command history/logs show a `git push` that embedded a GitHub credential directly in the URL.

Impact:
- Anyone with access to your machine profile, terminal logs, backups, or synced IDE state can recover the credential and obtain repo access.

Remediation (do now):
- Revoke the exposed GitHub token/credential immediately in GitHub settings.
- Rotate any other credentials that token could reach (private repos, packages, CI secrets).
- Purge local shell history entries referencing that token (and treat backups/sync targets as potentially contaminated).
- Move to one of:
  - SSH deploy keys / SSH agent, or
  - HTTPS with credential helper (Keychain) and **never** embed credentials in URLs.

Hardening:
- Add secret scanning in CI (GitHub Advanced Security or a lightweight scanner) and block pushes containing token patterns.

### 2) High — TLS verification disabled in Node (`NODE_TLS_REJECT_UNAUTHORIZED=0`) (operational)

Evidence:
- `npm audit` emitted a warning that TLS verification is disabled.

Impact:
- HTTPS connections do not validate certificates. Any dependency install, audit, or remote call can be intercepted and altered.

Remediation (do now):
- Remove `NODE_TLS_REJECT_UNAUTHORIZED=0` from your environment:
  - Shell profiles (`~/.bashrc`, `~/.bash_profile`, `~/.zshrc`)
  - CI environment variables
  - Any task runners / `.env` files used by Node scripts
- If you set it to work around corporate TLS interception, fix it properly:
  - install the correct CA bundle, or
  - configure Node to trust your org CA via `NODE_EXTRA_CA_CERTS` (preferred), not by disabling verification.

Policy/compliance note:
- Disabling TLS verification is generally non-compliant for any environment that fetches code or transmits credentials.

### 3) Medium — Missing explicit security headers / CSP at app level (deployment)

Evidence:
- `website/next.config.ts` is empty and there is no `middleware.ts` setting headers.

Impact:
- You rely on platform defaults. If hosting is misconfigured, you may ship without CSP/HSTS/anti-clickjacking protections.

Remediation (next change to code/deploy):
- Define security headers in `next.config.ts` via `headers()` for all routes, including:
  - `Content-Security-Policy` (start strict; adjust for fonts/images as needed)
  - `Strict-Transport-Security` (HSTS; only if you are HTTPS-only)
  - `X-Content-Type-Options: nosniff`
  - `Referrer-Policy: no-referrer` or `strict-origin-when-cross-origin`
  - `Permissions-Policy` (disable unused capabilities)
  - Prefer CSP `frame-ancestors` over `X-Frame-Options`

Verification:
- After deploy, verify headers with browser devtools / `curl -I` and a CSP evaluator.

### 4) Low — Secrets handling posture (repo hygiene)

Evidence:
- Root `.gitignore` ignores `.env`.
- `website/.gitignore` ignores `.env*`.

Risks:
- Accidental inclusion via other files (logs, JSON exports) and accidental copying into docs.

Hardening:
- Ensure `.env` is never committed and never copied into `website/` or `docs/`.
- Prefer `.env.example` with placeholders only (no real keys).
- Add a pre-commit secret scanner if you use git locally.

### 5) Informational — Frontend code risk profile looks clean

Observed:
- No `dangerouslySetInnerHTML`, `eval`, `document.write`, or storage/cookie usage in `website/src/`.
- No outbound network calls (`fetch`, websockets, XHR) detected in `website/src/`.
- No third-party scripts detected in `website/src/`.

Residual risk:
- If you later add markdown rendering, CMS content, analytics, or user input, re-audit for XSS, tracking, and consent requirements.

## Dependency status

- `npm audit` (website): **0 vulnerabilities found** at time of audit.

Hardening:
- Keep `package-lock.json` committed and use `npm ci` in CI to ensure deterministic builds.
- Enable automated dependency update PRs (Dependabot/Renovate) and require CI checks.

## Compliance notes (for a static informational site)

- Privacy: If no analytics, cookies, or form capture exist, your privacy obligations are minimal. If you add any telemetry, publish a privacy notice and capture consent where required.
- Security policy: Add a `SECURITY.md` (vulnerability disclosure) and a contact email/PGP key if you want responsible reporting.
- Licensing: Repo declares **MIT**; ensure third-party dependencies’ licenses are compatible (standard for npm, but still documentable).

## Immediate next actions (ordered)

1) Revoke the exposed GitHub credential and rotate related secrets.  
2) Remove `NODE_TLS_REJECT_UNAUTHORIZED=0` everywhere; replace with proper CA trust configuration if needed.  
3) Add explicit security headers + CSP in `website/next.config.ts`, then verify on the live domain.  
4) Add automated secret scanning and dependency update automation in your hosting/CI workflow.  

