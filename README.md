<br />
<div align="center">
  <h1 align="center">Budgetter</h1>
  <p align="center">
    🧾 Budgetter is a personal finance management software such as <a href="https://en.wikipedia.org/wiki/Microsoft_Money">Money</a>.
    <br />
    <br />
    <a href="https://github.com/opierre/Budgetter/issues">Report Bug</a>
    ·
    <a href="https://github.com/opierre/Budgetter/issues">Request Feature</a>
    <br />
    <br />    
    <a style="text-decoration:none" href="https://github.com/opierre/Budgetter/actions/workflows/pylint.yml" target="_blank">
      <img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/opierre/da061024a6dc8c3dcaf32f4e79abf032/raw/pylint.json">
    </a>
    <a style="text-decoration:none" href="https://sonarcloud.io/summary/new_code?id=opierre_Budgetter" target="_blank">
      <img src="https://sonarcloud.io/api/project_badges/measure?project=opierre_Budgetter&metric=alert_status">
    </a>
    <a style="text-decoration:none" href="https://sonarcloud.io/summary/new_code?id=opierre_Budgetter" target="_blank">
      <img src="https://sonarcloud.io/api/project_badges/measure?project=opierre_Budgetter&metric=vulnerabilities">
    </a>
    <a style="text-decoration:none" href="https://sonarcloud.io/summary/new_code?id=opierre_Budgetter" target="_blank">
      <img src="https://sonarcloud.io/api/project_badges/measure?project=opierre_Budgetter&metric=bugs">
    </a>
    <a style="text-decoration:none" href="https://sonarcloud.io/summary/new_code?id=opierre_Budgetter" target="_blank">
      <img src="https://sonarcloud.io/api/project_badges/measure?project=opierre_Budgetter&metric=security_rating">
    </a>
    <a style="text-decoration:none" href="https://sonarcloud.io/summary/new_code?id=opierre_Budgetter" target="_blank">
      <img src="https://sonarcloud.io/api/project_badges/measure?project=opierre_Budgetter&metric=sqale_rating">
    </a>
    <a style="text-decoration:none" href="https://sonarcloud.io/summary/new_code?id=opierre_Budgetter" target="_blank">
      <img src="https://sonarcloud.io/api/project_badges/measure?project=opierre_Budgetter&metric=reliability_rating">
    </a>
  </p>
</div>

---
Table of contents
=================

* [Production](#production)
    * [Packaging](#packaging)
    * [Installation](#installing)
* [How to Contribute](#howtocontribute)
* [Requirements](#requirements)

## <a name="production"></a> 🛠️ Production

### <a name="packaging"></a> Packaging

This software is delivered as a Python package and can be installed with following command line:

```bash
$ python -m build
```

### <a name="installing"></a> Installation

You can install *Budgetter* from current directory after cloning project:

```bash
$ cd budgetter
$ python -m pip install .
```

You can also install *Budgetter* from PyPi:

```bash
$ python -m pip install budgetter
```

Or you can also install *Budgetter* manually from [Releases](https://github.com/opierre/Budgetter/releases)

## <a name="howtocontribute"></a> 🧪 How to Contribute

* Clone current repo and create a new branch:

```bash
$ git checkout https://github.com/opierre/Budgetter -b new_branch_name
```

* Make changes and test
* Submit Pull Request with comprehensive description of changes

## <a name="requirements"></a> 📦 Requirements

See [requirements.txt](requirements.txt) and install:

```bash
$ python -m pip install -r requirements.txt
```
