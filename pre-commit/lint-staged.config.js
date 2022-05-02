module.exports = {
    "*.py": [
      "black",
      "flake8 --select F401",  // catches unused imports missed by running flake8 with diff-quality
      "git add"
    ],
    "js/**/\*.{js,jsx,json,css,md,ts,tsx}": [
      "bash -c 'cd js/ && yarn prettify-root-and-overwrite && lerna run --parallel --stream lint-staged && cd ../'",
      "git add"
    ],
}