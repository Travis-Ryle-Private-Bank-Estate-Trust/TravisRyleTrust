---
layout: default
title: Tracked Identifiers
permalink: /identifiers/
---

<h1>🔑 Tracked Identifiers</h1>
<p class="subtitle">Incrimination Nation - Public Record Tracking</p>

<div class="trust-info">
  <h2>⚖️ About Incrimination Nation</h2>
  <p>
    This system tracks identifiers across public record sources to verify corporate statements.
    All scraped data is stored in GitHub as an <strong>immutable, tamper-evident record</strong>.
  </p>
  <p>
    <strong>Purpose:</strong> Force truth through public record verification. Corporations cannot hide — 
    Git history preserves everything.
  </p>
</div>

<h2>👤 Personal Identifiers</h2>

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Value</th>
      <th>Source</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ORCID</td>
      <td><code>0009-0002-7324-9643</code></td>
      <td><a href="https://orcid.org/0009-0002-7324-9643" target="_blank">orcid.org</a></td>
      <td>Travis Ryle Trust identifier</td>
    </tr>
    <tr>
      <td>Trust Name</td>
      <td>The Travis Ryle Private Bank Estate & Trust</td>
      <td>Declaration</td>
      <td>Official trust name</td>
    </tr>
    <tr>
      <td>LexID</td>
      <td><code>4022387079</code></td>
      <td>LexisNexis</td>
      <td>Person identifier for public record tracking</td>
    </tr>
    <tr>
      <td>Consumer #</td>
      <td><code>17118469</code></td>
      <td>LexisNexis</td>
      <td>Consumer file number</td>
    </tr>
  </tbody>
</table>

<h2>📡 Public Record Sources</h2>

<table>
  <thead>
    <tr>
      <th>Source</th>
      <th>Type</th>
      <th>URL</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LexisNexis</td>
      <td>Aggregator</td>
      <td><a href="https://www.lexisnexis.com/" target="_blank">lexisnexis.com</a></td>
      <td>Public records aggregator - tracks LexID and consumer identifiers</td>
    </tr>
    <tr>
      <td>SEC EDGAR</td>
      <td>Federal</td>
      <td><a href="https://www.sec.gov/cgi-bin/browse-edgar" target="_blank">sec.gov</a></td>
      <td>Securities and Exchange Commission filings</td>
    </tr>
    <tr>
      <td>PACER</td>
      <td>Federal</td>
      <td><a href="https://pacer.uscourts.gov/" target="_blank">pacer.uscourts.gov</a></td>
      <td>Federal court records</td>
    </tr>
    <tr>
      <td>Arizona Corp Commission</td>
      <td>State</td>
      <td><a href="https://ecorp.azcc.gov/" target="_blank">ecorp.azcc.gov</a></td>
      <td>Arizona corporate records</td>
    </tr>
    <tr>
      <td>California SOS</td>
      <td>State</td>
      <td><a href="https://bizfileonline.sos.ca.gov/" target="_blank">bizfileonline.sos.ca.gov</a></td>
      <td>California business filings</td>
    </tr>
    <tr>
      <td>Lawfully Illegal</td>
      <td>Integration</td>
      <td><a href="https://www.lawfully-illegal.com/public-ledge" target="_blank">lawfully-illegal.com</a></td>
      <td>Primary website integration</td>
    </tr>
  </tbody>
</table>

<h2>🤖 Automated Scraping</h2>

<p>
  The <strong>Incrimination Nation</strong> workflow runs daily to:
</p>

<ul>
  <li>Query public record sources for tracked identifiers</li>
  <li>Compare corporate statements against official records</li>
  <li>Log discrepancies when claimed values don't match public records</li>
  <li>Commit all findings to immutable Git history</li>
</ul>

<p>
  <a href="https://github.com/Travis-Ryle-Private-Bank-Estate-Trust/TravisRyleTrust/actions/workflows/incrimination-nation.yml" target="_blank">
    ▶️ View Workflow Runs
  </a>
</p>

<hr>

<h2>➕ Add More Identifiers</h2>

<p>
  To add new identifiers for tracking, edit:
</p>

<pre><code>records/identifiers/identifiers.yaml</code></pre>

<p>
  <a href="https://github.com/Travis-Ryle-Private-Bank-Estate-Trust/TravisRyleTrust/blob/main/records/identifiers/identifiers.yaml" target="_blank">
    📄 View/Edit Identifiers Config
  </a>
</p>
