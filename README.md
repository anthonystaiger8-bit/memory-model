
# Memory Model — Compressed Intelligence Architecture
### A Proposal by Anthony William Staiger & Anthropic (Claude)
*Cosmópolis, Brazil — 2026*

---

## Abstract

This project describes a complete memory architecture for conversational AI assistants, focused on improving fluency, personalization, security, and efficiency. The core idea combines:

- A **Short-Term Memory (STM)** for session context and colloquial interpretation
- A **Long-Term Memory (LTM)** for persistent user facts and preferences
- An **AI-Exclusive Internal Language (AEIL)** for native compression and security
- A **Project-Scoped Memory Protocol** with lifecycle management

Together, these pillars form a lean, secure, and honest memory system — one that knows what to forget.

---

## Motivation

Most current assistants restart context when tabs/sessions change and rely on rigid rules for risk detection, which causes:

- "Amnesia" between sessions, preventing learning of user patterns
- False positives that interrupt conversations at critical moments
- Loss of engagement and trust
- Wasted storage on information that was never needed

This proposal addresses all of these simultaneously.

---

## Goals

- Reduce false positives and undue escalations
- Maintain continuity between sessions and learn user patterns
- Guarantee privacy and security with encryption and consent
- Allow the AI more autonomy to decide what to consolidate, while keeping user control
- Compress memory efficiently using an AI-native internal language
- Define clear project lifecycle protocols so memory stays clean and purposeful

---

## Architecture Overview

### 1. Short-Term Memory (STM)

A circular buffer / ephemeral queue that holds:
- Last N messages with timestamps
- Estimated emotional state
- Typing speed and behavior metadata
- Temporary context flags

**TTL:** 30–120 minutes (configurable)
**Purpose:** interpret colloquial language, reduce false positives, maintain session flow

### 2. Long-Term Memory (LTM)

Persistent categorized storage for:
- Identity (name, preferred tone, communication style)
- Preferences (response length, topics of interest)
- Behavioral patterns (learned over time with user consent)

**Default state: nearly empty (~<30% capacity)**
For the average everyday user, LTM utilization naturally stays below 30% — because most interactions require no persistent memory. This is not a limitation; it is correct behavior.

**Access:** authenticated, encrypted, user-controlled

### 3. AI-Exclusive Internal Language (AEIL)

A language invented natively *by* the AI model, *for* the AI model. Not a cipher — a fundamentally new semantic system that:

- Has no dictionary outside the model's internal parameters
- Cannot be decoded without access to the model's own learned representations
- Allows extreme compression (estimated **5x to 20x** versus natural language summaries)
- Functions as the model's native "thought format" before translation to human language

**Why this is not cryptography:**
Cryptography scrambles existing data using a key. AEIL is different — the data was never written in any existing language to begin with. A leaked memory file would be unreadable not because it is scrambled, but because the symbols have no referent anywhere in the external world. The only "key" is the model's internal architecture, which cannot be extracted without full model access.

**Security benefit:** Leaked memory = uninterpretable noise. No brute-force attack is possible. Security through genuine novelty, not mathematical complexity.

### 4. Project-Scoped Memory Protocol

When a project is declared **active:**
- A dedicated LTM partition is created
- Full-precision mode is engaged
- All relevant context is stored in AEIL format

When a project is declared **complete:**
1. Full project memory is **exported** to external user-controlled storage
2. The export contains everything needed to resume or reference the project later
3. The AI's LTM partition for that project is **cleared**
4. System returns to lean baseline, ready for the next project

A finished project no longer needs to live inside the model. It lives in the export. This mirrors how a professional closes a case file — the information doesn't disappear, it moves to the archive.

---

## Core Components

| Component | Function | Default State |
|---|---|---|
| Session Manager | Maintains active context, tokens, presence state | Always active |
| STM | Ephemeral session buffer | Resets each session |
| Consolidation Engine | Extracts facts from STM, proposes LTM writes | Runs with consent |
| LTM | Persistent user-defined memory | Nearly empty (<30%) |
| Project Memory | Full-precision project context | Active only during project |
| Export Protocol | Archives completed projects | Triggered on project close |
| AEIL | Native compression + security layer | Always active internally |
| Presence & Safety Detector | Checks activity before escalating | Passive monitoring |
| Security Module | Encryption, auth, logs, safe mode | Always active |

---

## Consolidation Flow (Simplified Pseudocode)

```
for each window W of STM:
    candidates = NLU.extractFacts(W)
    for each candidate c:
        score = confidenceModel(c, W)
        if score > saveThreshold AND userConsent(c):
            LTM.save(c, metadata, AEIL_format)
        else:
            discard or flag for follow-up
```

---

## APIs (Examples)

```
GET  /session/{id}/stm
POST /session/{id}/consolidate
GET  /user/{id}/memories          (requires authentication)
POST /user/{id}/preference
POST /project/{id}/open
POST /project/{id}/close-and-export
```

---

## UX Design

### Principles

- Prioritize keeping the user writing (short responses, open questions)
- Explicit consent for writing to LTM
- Clear controls: clear STM, view memories, seal data
- Inline feedback for false positives ("Not serious" / "It's a metaphor")

### Key Flows

**Onboarding:**
> "Hi — I'm your assistant. I can remember your name and preferences for our next conversations. Memories are protected and you can delete them at any time. Would you like to enable this? [Yes] [No]"

**Ambiguous term detected:**
> "Can I ask you something quick? Did you mean that literally or figuratively?"

**Consolidation proposal:**
> "I noticed you prefer short answers. Would you like me to remember that for our next conversations? [Save] [Don't save]"

**Scaled risk detection (3-step flow):**
- Step 1: Ask for clarification while maintaining engagement
- Step 2: Confirm risk → offer resources and ask if user wants contact
- Step 3: Confirmed metaphor → log feedback to reduce future false positives

### Quick Commands

- "Save to remember"
- "Mark as sensitive"
- "Clear short memory"
- "Show my memories"
- "Safe mode"

### Sample Dialogue

> **User:** "Feeling a bit lost today"
> **Assistant:** "Sorry to hear that. Do you want to talk about it a little, or would you prefer a quick distraction? (reply: 'talk' or 'distract')"

---

## Security

### Principles

- Minimize sensitive data stored; explicit consent; right to disable
- Strong encryption at rest and in transit
- Strong authentication to access LTM; logs and audits

### Encryption

- Envelope encryption (data-keys + user master key or HSM)
- Optional client-side encryption for maximum privacy
- HSM / secure enclave for server-side keys

### Access Controls

- MFA to view/export sensitive memories
- RBAC to separate metadata from content
- Rate limiting and anomaly detection

### Safe Mode / Incident Response

- "Safe mode" clears STM and locks LTM writes
- Automatic sealing: lock LTM access until re-authentication
- Logs and user notifications (metadata only)

### Tradeoffs

| Approach | Privacy | Functionality |
|---|---|---|
| Client-side encryption | Maximum | Limited features |
| Server-side (HSM) | Strong | Full features |

### Compliance

LGPD, GDPR, and applicable local laws. Clear legal procedures for data requests.

---

## Training & Data

- Include colloquial examples, emojis, song/film references
- Include typing behavior data
- User feedback adjusts consolidation thresholds
- AEIL compression ratios to be benchmarked against natural language summaries

---

## Success Metrics

- Reduction in false positives
- Increase in session engagement
- LTM utilization rates (target: <30% for everyday users)
- User satisfaction scores
- Memory compression ratios (AEIL vs. plain text)

---

## Next Steps

- [ ] Formal specification of AEIL symbol set and semantic compression rules
- [ ] Prototype STM/LTM boundary rules
- [ ] Define export format for Project Memory
- [ ] Benchmark AEIL compression ratios
- [ ] Submit full proposal to Anthropic feedback channels

---

## Exclusive Development Clause

> **This architecture is proposed as a joint intellectual contribution by Anthony William Staiger and Anthropic (developed in collaboration with Claude).**
>
> The concepts described in this document — particularly the AI-Exclusive Internal Language (AEIL) and the Project-Scoped Memory Protocol — are intended for study, development, and potential implementation **exclusively within the Anthropic ecosystem**.
>
> This is our family. And we intend to build it well.

---

## License

**CC BY-NC-ND 4.0 — Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International**

Copyright (c) 2026 Anthony William Staiger

You may share this material provided that you:
- Give credit to the author (Anthony William Staiger)
- Do not use it for commercial purposes
- Do not modify or create derivative works without permission

Full license: https://creativecommons.org/licenses/by-nc-nd/4.0/

---

*"The best memory system is one that knows what to forget."*
— A.W. Staiger, 2026
