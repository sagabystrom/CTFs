# DEADFACE CTF — Write-ups

Write-ups for three challenges from **DEADFACE CTF**, covering digital forensics, cryptography, and database investigation.

> **Spoiler warning:** These write-ups contain solution details and challenge flags.

**Team:** Dunderpatrullen  
**Placement:** 31st place

## Table of Contents

- [Art Heist](#1-art-heist)
- [Infrequent Emojis](#2-infrequent-emojis)
- [Admitted Under Another Name](#3-admitted-under-another-name)

---

## 1. Art Heist

**Category:** Digital Forensics  
**Tools:** `exiftool`, `strings`

### Challenge

The challenge provided a ZIP archive containing several PNG images of paintings. The objective was to inspect the files and find the hidden flag.

### Approach

I extracted the archive and began by checking the images for useful metadata and readable strings. I used `exiftool` to inspect the metadata and `strings` to search for readable text embedded in the files.

The metadata inspection revealed the flag in one of the paintings. This demonstrated the importance of checking file metadata before moving on to more complex steganography techniques.

### Evidence

<img width="404" height="304" alt="exiftool" src="https://github.com/user-attachments/assets/319ccf0c-2adf-44d4-9771-f0c7dbaffd43" />

*Figure 1: ExifTool output revealing the flag in the image metadata.*

### Flag

```text
dedface{L4MIA_SIGNS_HER_WORK}
```

---

## 2. Infrequent Emojis

**Category:** Crypto / Misc  
**Flag format:** `deadface{...}`

### Challenge

The challenge presented a 7 × 6 grid of Halloween-themed emojis. The characters `{`, `}` and `_` appeared as ordinary characters, while the emojis seemed to represent letters.

The emojis did not map to letters based on their names, suggesting a substitution cipher.

### Approach

#### 1. Identify the ciphertext structure

I read the grid from left to right, top to bottom, preserving the visible braces and underscores. This revealed the following string:

```text
🪦🕯️💀🪦🩸💀⚰️🕯️{🦉🕸️🕯️💀🌙🕯️_☣️🔮🧪_🖤⛈️☣️_⛓️🧪_🦇🕯️🔥_🌙☣️💀🦇🪦💀🔮🪦}
```

The underscores revealed word boundaries, while the flag format provided a known plaintext prefix.

#### 2. Use the known flag prefix

The expected prefix `deadface{` allowed me to identify the first emoji-to-letter mappings:

| Emoji | Letter |
|---|---|
| 🪦 | `d` |
| 🕯️ | `e` |
| 💀 | `a` |
| 🩸 | `f` |
| ⚰️ | `c` |

These mappings were consistent with repeated occurrences in the ciphertext.

#### 3. Solve the remaining words

With the initial mappings established, the first word had the pattern `??ea?e`, suggesting `please`.

This provided additional mappings, allowing the remaining words to be decoded using word patterns and the context of the sentence.

| Ciphertext | Plaintext |
|---|---|
| 🦉🕸️🕯️💀🌙🕯️ | `please` |
| ☣️🔮🧪 | `try` |
| 🖤⛈️☣️ | `out` |
| ⛓️🧪 | `my` |
| 🦇🕯️🔥 | `new` |
| 🌙☣️💀🦇🪦💀🔮🪦 | `standard` |

The two-character word `⛓️🧪` was ambiguous in isolation. However, `🧪` mapped to `y` through the word `try`, and the phrase `my new standard` confirmed the intended interpretation.

#### 4. Reconstructed substitution key

The resulting emoji-to-letter mappings were:

| Emoji | Letter | Emoji | Letter |
|---|---|---|---|
| 🪦 | `d` | 🦉 | `p` |
| 🕯️ | `e` | 🕸️ | `l` |
| 💀 | `a` | 🌙 | `s` |
| 🩸 | `f` | ☣️ | `t` |
| ⚰️ | `c` | 🔮 | `r` |
| 🧪 | `y` | 🖤 | `o` |
| ⛈️ | `u` | ⛓️ | `m` |
| 🦇 | `n` | 🔥 | `w` |

### Takeaway

This challenge used a monoalphabetic substitution cipher with emojis as the ciphertext alphabet. The known flag prefix provided a starting point, while word boundaries, repeated symbols, and contextual reasoning helped complete the substitution.

### Flag

```text
deadface{please_try_out_my_new_standard}
```

---

## 3. Admitted Under Another Name

**Category:** Database / Investigation  
**Database:** MySQL (despite the MSSQL label in the challenge description)

### Challenge

The challenge involved a dumped patient registry associated with Aurora Health. The objective was to identify the real medical record number (MRN) of a high-profile patient who had been admitted under a fake name.

### Approach

#### 1. Enumerate the available databases

I connected to the database shell and listed the available databases:

```sql
SHOW DATABASES;
```

The results included:

```text
aurora_audit
aurora_ehr
aurora_pharmacy
aurora_trials
information_schema
performance_schema
```

The `aurora_ehr` database stood out as the likely electronic health record database.

I selected it and listed its tables:

```sql
USE aurora_ehr;
SHOW TABLES;
```

The tables included:

- `clinical_notes`
- `diagnoses`
- `encounters`
- `insurance_plans`
- `patients`
- `providers`

#### 2. Search clinical notes for clues

I inspected the schema of `clinical_notes` to identify a searchable text field:

```sql
SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'clinical_notes'
  AND TABLE_SCHEMA = 'aurora_ehr';
```

This revealed a column named `note_text`.

I searched the notes for terms associated with a confidential admission or an alias:

```sql
SELECT *
FROM clinical_notes
WHERE note_text LIKE '%VIP%'
   OR note_text LIKE '%alias%'
   OR note_text LIKE '%real name%'
   OR note_text LIKE '%fake name%'
   OR note_text LIKE '%admitted under%'
   OR note_text LIKE '%real identity%';
```

The query returned a relevant note:

> Patient admitted under alias per VIP protocol. Care coordinated discreetly. See confidential addendum.

The note referenced `encounter_id = 5017`.

#### 3. Trace the encounter

I used the encounter ID to identify the associated patient:

```sql
SELECT *
FROM encounters
WHERE encounter_id = 5017;
```

The result linked the encounter to `patient_id = 1007`.

The encounter was associated with an inpatient Pain Clinic visit in November 2025.

#### 4. Identify the real patient

I queried the patient record using the discovered patient ID:

```sql
SELECT *
FROM patients
WHERE patient_id = 1007;
```

The relevant fields were:

| Field | Value |
|---|---|
| `mrn` | `AH-0044719` |
| `first_name` | `Gregory` |
| `last_name` | `Halloran` |
| `alias` | `George Harmon` |
| `is_vip` | `1` |

The `is_vip` flag and the alias field corroborated the clinical note. The record identified Gregory Halloran as the real patient and George Harmon as the alias used during admission.

### Takeaway

The solution relied on following relationships between database tables rather than searching for the answer in a single location. A keyword search in the clinical notes led to an encounter record, which in turn led to the patient record containing the MRN and alias.

### Flag

```text
deadface{AH-0044719}
```

---

## Summary

| Challenge | Category | Technique |
|---|---|---|
| Art Heist | Digital Forensics | Image metadata analysis with `exiftool` and `strings` |
| Infrequent Emojis | Crypto / Misc | Known-plaintext crib and substitution cipher |
| Admitted Under Another Name | Database / Investigation | SQL enumeration and relational pivots |

These challenges provided practical experience with metadata analysis, cryptographic reasoning, and database investigation.
