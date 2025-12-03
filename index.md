---
layout: default
title: Home
---

<div class="home">
  <h1>🏛️ The Travis Ryle Private Bank Estate & Trust</h1>
  <p class="subtitle">Public-Facing Ledger & Incrimination Nation Tracking System</p>

  <div class="trust-info">
    <h2>📜 Trust Declaration</h2>
    <p>
      Declared by <strong>Travis Steven Ryle</strong>, Ambassador in Christ, Grantor, Guarantor, and Beneficiary.
    </p>
    <p>
      <a href="https://orcid.org/0009-0002-7324-9643" target="_blank">📎 ORCID Record</a> |
      <a href="https://www.lawfully-illegal.com/public-ledge" target="_blank">📊 Public Ledge</a> |
      <a href="https://www.lawfully-illegal.com/tracking" target="_blank">🔍 Tracking</a>
    </p>
  </div>

  <hr>

  <h2>⚖️ Incrimination Nation</h2>
  <p>
    <em>Forcing truth through public record verification.</em>
  </p>
  <p>
    This system scrapes public records and stores them in GitHub as an <strong>immutable, tamper-evident record trail</strong>.
    Corporations cannot hide from public records — Git history preserves everything.
  </p>

  <h3>🔑 Tracked Identifiers</h3>
  <table>
    <thead>
      <tr>
        <th>Type</th>
        <th>Value</th>
        <th>Source</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ORCID</td>
        <td>0009-0002-7324-9643</td>
        <td>orcid.org</td>
      </tr>
      <tr>
        <td>LexID</td>
        <td>4022387079</td>
        <td>LexisNexis</td>
      </tr>
      <tr>
        <td>Consumer #</td>
        <td>17118469</td>
        <td>LexisNexis</td>
      </tr>
    </tbody>
  </table>

  <hr>

  <h2>📋 Public Ledger Entries</h2>
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Action</th>
        <th>Party</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>LED-20251123-004</td>
        <td>Public record inquiry: Kingman court</td>
        <td>Mohave County / Kingman</td>
        <td>🟡 Open</td>
      </tr>
      <tr>
        <td>LED-20251123-005</td>
        <td>Entity dossier: Aztec Constructors</td>
        <td>Corporate records</td>
        <td>🟡 Open</td>
      </tr>
      <tr>
        <td>LED-20251123-006</td>
        <td>County records inquiry: Contra Costa</td>
        <td>Contra Costa County</td>
        <td>🟡 Open</td>
      </tr>
    </tbody>
  </table>

  <hr>

  <h2>🔗 External Links</h2>
  <ul>
    <li><a href="https://www.lawfully-illegal.com" target="_blank">Lawfully Illegal - Main Site</a></li>
    <li><a href="https://www.lawfully-illegal.com/public-ledge" target="_blank">Public Ledge</a></li>
    <li><a href="https://www.lawfully-illegal.com/tracking" target="_blank">Tracking System</a></li>
    <li><a href="https://github.com/Travis-Ryle-Private-Bank-Estate-Trust/TravisRyleTrust" target="_blank">GitHub Repository (Immutable Record)</a></li>
  </ul>

  <hr>

  <h2>📁 Repository Structure</h2>
  <ul>
    <li><code>records/</code> - All tracked records and identifiers</li>
    <li><code>records/identifiers/</code> - LexisNexis and other ID tracking</li>
    <li><code>records/public-ledger/</code> - Public ledger entries</li>
    <li><code>records/scraped/</code> - Scraped public record snapshots</li>
    <li><code>notices/</code> - Legal notices</li>
    <li><code>communications/</code> - Email and correspondence tracking</li>
  </ul>

  <footer>
    <p>
      <strong>⚠️ NOTICE:</strong> All records in this repository are part of immutable Git history.
      They cannot be destroyed or altered without creating a permanent audit trail.
    </p>
    <p>
      <em>Last updated: {{ site.time | date: "%Y-%m-%d %H:%M UTC" }}</em>
    </p>
  </footer>
</div>

<style>
  .home {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
  }
  .subtitle {
    color: #666;
    font-style: italic;
    margin-bottom: 30px;
  }
  .trust-info {
    background: #f5f5f5;
    padding: 20px;
    border-radius: 8px;
    margin: 20px 0;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
  }
  th {
    background: #333;
    color: white;
  }
  tr:nth-child(even) {
    background: #f9f9f9;
  }
  footer {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 2px solid #333;
    font-size: 0.9em;
  }
  code {
    background: #eee;
    padding: 2px 6px;
    border-radius: 3px;
  }
</style>
