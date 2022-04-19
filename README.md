# S-Reporter

S-Reporter allows you to export scan results from Snyk to excel file. It gives you your excel output on a project basis.
## Downloading and Running

### First of All

-You should go to your project page.

For example:

https://app.snyk.io/org/[your_snyk_username]/project/[your_project_code]

![snyk](https://user-images.githubusercontent.com/29353162/163973162-b2a91618-0f42-4a53-a8bf-c7b1085f6fc3.png)

And save this page in your local repo folder as html.

<img width="619" alt="examplehtml" src="https://user-images.githubusercontent.com/29353162/163973430-88f51807-5c38-4108-abc4-d1a6cf241480.png">

And you will see your report in report folder when the program finishes running.

<img width="1440" alt="Screen Shot 2022-04-19 at 02 24 53" src="https://user-images.githubusercontent.com/29353162/163973732-76d7e83b-72ab-4517-a778-40d1933048ef.png">

<img width="619" alt="Screen Shot 2022-04-19 at 02 33 42" src="https://user-images.githubusercontent.com/29353162/163973763-f915aec0-3a6c-46f0-9c91-e5f1c34873ec.png">


### For Windows:

Clone the project

```bash
  git clone https://github.com/cagrialis/s-reporter.git
```

Open your command prompt

Run this command

```bash
  python [YOUR_LOCAL_REPO_PATH] [YOUR_REPORT_PAGE_HTML]
```

For Example

```bash
  python B:\basic-password-generator\main.py B:\basic-password-generator\example.html
```

### For Linux:

Clone the project

```bash
  git clone https://github.com/cagrialis/s-reporter.git
```

Go your local folder

```bash
  cd s-reporter
```

Run this command

```bash
  python3 main.py [YOUR_REPORT_PAGE_HTML]
```

For Example

```bash
  python3 main.py example.html
```
