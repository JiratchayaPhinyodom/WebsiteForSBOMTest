# Python Project SBOM & Automated Security

This project demonstrates **SBOM generation** and **automated vulnerability scanning** for a Python project using **CycloneDX** and **pip-audit**.

---

## 📦 Software Bill of Materials (SBOM)

We generate a **CycloneDX SBOM (`bom.json`)** for all Python dependencies, including direct and transitive packages.
The SBOM provides:

* **Package name and version**
* **Type** (library/application)
* **Dependency relationships**
* **Metadata** about the SBOM generator (tool, version, timestamp)

**Purpose:**
The SBOM enables **supply chain transparency**, **license compliance**, and **auditing**. It tells exactly what is installed in your project so security tools can analyze it.

---

## 🔒 Vulnerability Scanning with pip-audit

We use **`pip-audit`** to scan all installed packages for **known vulnerabilities**. This produces a **`report.json`** containing:

* **Dependencies** scanned
* **Vulnerabilities** detected, including CVE/GHSA IDs, descriptions, and fix versions

Example:

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

**Relationship to SBOM:**

* The **SBOM lists what packages exist**
* The **pip-audit report analyzes those packages for risk**
* Together, they give **full supply chain security visibility**

---

## ⚙️ CI/CD Integration

Using **GitHub Actions**, the workflow:

1. Installs dependencies from `requirements.txt`
2. Generates the SBOM (`bom.json`)
3. Runs `pip-audit` and produces a vulnerability report (`report.json`)
4. Automatically **fails the workflow** if vulnerabilities exist (e.g., HIGH/CRITICAL severity)
5. Uploads both **SBOM and vulnerability report** as artifacts

This ensures **automated security checks** every time code is pushed.

---

## 🔧 How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Generate SBOM
cyclonedx-py requirements -i requirements.txt -o bom.json

# Run vulnerability scan
pip install pip-audit
pip-audit --format json -o report.json
```

---

## 🔹 Key Benefits

* **Automated supply chain security**
* **Early detection of vulnerable packages**
* **Traceable, auditable dependency information**
* **Supports compliance and DevSecOps practices**
