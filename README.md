# Mapping Fossil Ties Web portal

## 1. Project setup

### 1.1. Requirements and setup:

This needs NPM and nodeJS - information on installing can be found [here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

Clone the repository and then install all necessary packages:
```
git clone https://github.com/ronniep/uk-unis.git
cd uk-unis
npm install
```

### 1.2. Compile and test

From the root folder (`uk-test`) or any subfolder run:
```
npm run serve
```

### 1.3. Compile and deploy

From the root folder (`uk-test`) run:
```
npm run build
cd ./dist
rsync -e "ssh -p 7685" -rav * id2787836@solid-sustainability.org:/home/id2787836/domains/mappingfossilties.org/public_html/uktest/
```

You will have to enter a password. You can get it from me.

### 1.4. Lints and fixes files

```
npm run lint
```

### 1.5. Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## 2. Updating database

### 2.1. Updating when you have new ties

When you have new ties:

1) add the required information in the [google sheets ties list](https://docs.google.com/spreadsheets/d/12YfN9YbzxQqHVfB4JPXAdCGJNL8ZgSnt_WQ0QA0Yi3s/edit#gid=750502099) (check the tab "Info" if you are unsure how to input data) and ask someone to check and set the leftmost column to "1".
2) download the google sheets media list as a csv (go to File >> Download >> Comma Separated Values (.csv) )
3) navigate to the `media` folder and run the script `update_latest.sh`
4) note that data will only appear on the website if the "checked" column is set to "1".

### 2.2. Updating when you have new media

When you have new media:

1) add the new URL as well as required fields in the [google sheets media list](https://docs.google.com/spreadsheets/d/12YfN9YbzxQqHVfB4JPXAdCGJNL8ZgSnt_WQ0QA0Yi3s/edit#gid=55578901).
2) download the google sheets media list as a csv (go to File >> Download >> Comma Separated Values (.csv) )
3) navigate to the `media` folder and run the script `update_latest.sh`
4) it can be that the title, cover image and/or date are not recovered by this script, which results in missing information or pictures in the news overview page (`<root page>`/News.html). If that is the case, you need to input the title, cover image and/or date for this entry in the google sheets media list, and run steps 2 and 3 again.

### 2.3 Updating when you have new universities

When the list of universities change: 

- update the list in [the google sheets overview](https://docs.google.com/spreadsheets/d/12YfN9YbzxQqHVfB4JPXAdCGJNL8ZgSnt_WQ0QA0Yi3s/edit#gid=1977986785).
- download the google sheets overview as a csv (go to File >> Download >> Comma Separated Values (.csv) )
- navigate to the `media` folder and run the script `update_uni_list_in_code.sh`
- copy the generated output in `uniList.txt` and paste to replace lines 98 and 99 in file `../src/AppNews.vue` and lines 89 and 90 in file `../src/components/UniData.vue`.