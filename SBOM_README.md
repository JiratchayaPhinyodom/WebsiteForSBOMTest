# Software Bill of Materials (SBOM)

This project generates a CycloneDX SBOM (bom.json) for the Python dependencies of your project. The SBOM provides a complete, machine-readable list of all packages and their versions, including direct and transitive dependencies. It enables vulnerability scanning, license compliance checks, and supply chain transparency, helping teams quickly identify risky packages (e.g., requests==2.31.0 with known CVEs) and maintain a secure, auditable Python environment.

---

# 📄 `pip-audit` and `report.json`

1. **What it is**

   * `pip-audit` is a Python tool that **scans your installed packages for known vulnerabilities**.
   * It compares package versions in your environment (or `requirements.txt`) against security databases like **PyPI advisories** and **CVE/GHSA records**.

2. **What `report.json` contains**

   * **Dependencies**: Each Python package installed.
   * **Vulnerabilities**: For each package, details of CVEs or GHSA advisories, including:

     * `id` (CVE or GHSA)
     * `description`
     * `fix_versions` (versions that patch the vulnerability)
   * Example snippet:

```json
{
  "name": "requests",
  "version": "2.31.0",
  "vulns": [
    {
      "id": "CVE-2024-35195",
      "fix_versions": ["2.32.0"],
      "description": "TLS verification may remain disabled for subsequent requests..."
    }
  ]
}
```

3. **Purpose / Use**

   * Automatically **detects vulnerabilities** in your dependencies.
   * Can **fail CI/CD pipelines** if any critical issues are found.
   * Works together with `bom.json` to **verify the security of all components** in your Python project.

---

# 🔹 Relationship to SBOM

* **`bom.json` (SBOM)** lists **all dependencies and versions**, but does **not include vulnerability data** by itself.
* **`report.json` from pip-audit** is **a vulnerability analysis of those dependencies**.
* Together, they provide **full supply chain security**:

```
SBOM (bom.json) → tells what you have
pip-audit report (report.json) → tells what is risky / vulnerable
```

**`report.json` is not part of the SBOM**, but it is **used to audit the components listed in the SBOM**.

