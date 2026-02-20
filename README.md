# WebsiteForSBOMTest

This is a simple Python project demonstrating how to generate a **Software Bill of Materials (SBOM)** using **CycloneDX** and GitHub Actions.

---

## Project Structure

```

sample-sbom-project/
├── app.py
├── requirements.txt
└── .github/
└── workflows/
└── sbom.yml

````

- `app.py` – Simple Python app using requests, FastAPI, Uvicorn, NumPy, and pandas.  
- `requirements.txt` – Lists project dependencies.  
- `.github/workflows/sbom.yml` – GitHub Actions workflow to generate SBOM.

---

## Dependencies

```text
requests==2.31.0
fastapi==0.129.0
uvicorn==0.41.0
pandas==3.0.1
numpy==2.4.2
````

---

## GitHub Actions Workflow

The workflow automatically:

1. Runs on every push to the main branch (or can be manually triggered).
2. Checks out the repository.
3. Installs dependencies and/or uses `requirements.txt`.
4. Generates an SBOM (`bom.json`) using the **CycloneDX Python tool**.
5. Uploads the SBOM as an artifact for download.

**Key YAML Snippet:**

```yaml
name: Generate Python SBOM

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  sbom:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install CycloneDX
        run: pip install cyclonedx-bom
      - name: Generate SBOM
        run: cyclonedx-py requirements -i requirements.txt -o bom.json
      - name: Upload SBOM artifact
        uses: actions/upload-artifact@v4
        with:
          name: sbom-file
          path: bom.json
```

---

## How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Install CycloneDX tool
pip install cyclonedx-bom

# Generate SBOM
cyclonedx-py requirements -i requirements.txt -o bom.json
```

---

## SBOM Output

The workflow generates a file `bom.json` (CycloneDX 1.6 format) that includes:

* Project dependencies (`requests`, `fastapi`, `uvicorn`, `pandas`, `numpy`)
* Dependency versions
* Package URLs (PURL)
* Metadata about the SBOM tool

Example:

```json
{
  "components": [
    {"name": "fastapi", "version": "0.129.0"},
    {"name": "numpy", "version": "2.4.2"},
    {"name": "pandas", "version": "3.0.1"},
    {"name": "requests", "version": "2.31.0"},
    {"name": "uvicorn", "version": "0.41.0"}
  ]
}
```

---

## Notes

* GitHub Action uses `actions/upload-artifact@v4` (latest supported version).
* Workflow can be triggered manually via the **Actions** tab.
* SBOM can be used for **supply chain security**, vulnerability scanning, or artifact auditing.

---

## References

* [CycloneDX Python Tool](https://github.com/CycloneDX/cyclonedx-python)
* [CycloneDX SBOM Specification](https://cyclonedx.org/specification/)
* [GitHub Actions Documentation](https://docs.github.com/actions)

