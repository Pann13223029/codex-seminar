---
name: source-check
description: Check that every reference and citation in a draft is real and matches what the draft says. Finds each source online (doi.org, Crossref, OpenAlex, CiNii, J-STAGE, publisher or library pages), compares authors, year, title and journal, flags references that cannot be found or do not match (possibly made up by AI), and can check whether a source supports the sentence that cites it. Use when the user asks to check, verify or review references, citations, sources or a bibliography, or to find invented or AI-generated references. Do not use for formatting a reference list into a citation style or for writing new text.
---

# Source check

Find out, for each source a draft cites, whether it really exists and says
what the draft claims. AI tools can produce references that look real but
do not exist, or real papers with the wrong authors, year or DOI. The
student is responsible for every source in their work, so this check reports
what it found and never fills gaps. Reply in the language the user writes in
(for example Japanese or English).

## Inputs

- The draft (Word, Markdown, text or PDF) with its reference list, in the
  project folder. If there are several drafts, ask which one.
- Whether the user also wants the claim check (step 5). Ask if unclear.

## Steps

0. **Ask before going online.** Checking needs the internet. Tell the user
   that only the reference details (title, authors, year, DOI) will be sent
   to the search sites, never the draft text, and ask permission. If they
   say no, skip to step 6 and make the offline checklist.
1. **List the references.** Extract every entry in the reference list and
   every in-text citation, and number them. Report how many there are, and
   list:
   - citations with no matching entry in the reference list;
   - reference entries that are never cited in the text.
   Do not change any file.
2. **Look up each reference.** One at a time:
   - **Has a DOI:** open `https://doi.org/<DOI>` and the Crossref record
     `https://api.crossref.org/works/<DOI>`. A DOI that returns "not found"
     is a red flag.
   - **No DOI, article or paper:** search Crossref
     (`https://api.crossref.org/works?query.bibliographic=<title and first author>&rows=5`)
     and OpenAlex (`https://api.openalex.org/works?search=<title>`).
   - **Japanese source:** search CiNii Research
     (`https://cir.nii.ac.jp/opensearch/all?q=<title>&format=json`) and
     J-STAGE.
   - **Book:** the publisher's page, CiNii Books or the National Diet
     Library catalogue.
   - **Web page or report:** open the URL. Check that the page exists and
     that its title and organisation match.
   A search result is not a match just because it ranks first: compare the
   title, authors and year before accepting it. Stop after about three
   searches for one reference.
3. **Compare the details.** For the record you found, compare title,
   authors, year, journal or publisher, volume and pages, and DOI with what
   the draft says.
4. **Give each reference a status:**
   - **Verified:** a record was found and the title, first author and year
     match.
   - **Small differences:** the source exists, but some details differ (for
     example the year, pages or an author's spelling). Show the values from
     the record.
   - **Mismatch:** the DOI points to a different work, or the title exists
     with different authors or a different journal. Often two sources mixed
     together.
   - **Not found:** no matching record after searching at least two places.
     It may be invented. Say where you searched.
   - **Not checked [CHECK]:** no access, or the site did not answer. Say
     why.
5. **Check the claims (if the user wants).** For each sentence that cites a
   Verified source, read the abstract or the page and say whether it
   supports the sentence: **Supports**, **Partly**, **Does not support** or
   **Can't tell** (for example, only the title is available). Quote one short
   phrase from the abstract as evidence, with the link.
6. **Write the report.** Save `outputs/source-check.md` (if it exists, ask
   before replacing it) with:
   - the counts for each status;
   - a table: number, the reference as written, status, what was found (with
     the link), the differences, and what the user should do;
   - the claim check, if done;
   - if the user did not allow the internet: the same table with status
     "Not checked [CHECK]" and a search link for each reference (doi.org,
     Google Scholar, CiNii), so the user can check by hand.
7. **Tell the user what to do next:** open every Not found, Mismatch and
   Does not support item themselves; never cite a source they have not seen;
   and remove or replace (by their own search) any source that cannot be
   found.

## Rules

- Never mark a source Verified unless you opened a record of it in this
  session (DOI resolver, database or publisher page). Give the link.
- Never invent, suggest or fill in a replacement source, author, year, page
  or DOI. If the user asks for a replacement, give search words only.
- A source that exists can still be cited wrongly. Verified means the
  source is real, not that the sentence is right.
- Never change the draft or its reference list unless the user asks. If
  asked, change only details copied exactly from the record you found, and
  list each change.
- Send only reference details to websites, never the draft text or personal
  data.
- Be polite to the sites: one request at a time, and no more than about
  three searches per reference.
