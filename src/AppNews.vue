<template>
  <div class="house" id="mainContent">

    <div class="midcontainer">
      <MenuBar />
    </div>
    <div class="bigMidcontainer">

      <div class="titlediv extraspace">
        <h1>Fossil Ties in the Media</h1>
      </div>
      <div class="bodydivNews">

        <div class="filtersLeft">
          <FaqExpandable>
            <template #header>
              Filter results
            </template>
            <template #default>

              <div class="groupFilters">
                <div class="halfWidth">
                  <div class="checklistClass">
                    <input type="checkbox" checked id="allCat" @click="selectAllCat()">
                    <p class="checklistItem"><b>Select all categories</b></p>
                  </div>
                  <div v-for="item in arrCatFull" :key="item.shortCat" class="checklistClass">
                    <input type="checkbox" checked :id="item.shortCat" @click="changeCat()">
                    <p class="checklistItem">{{ item.longCat }}</p>
                  </div>
                </div>

                <div class="halfWidth">
                  <div class="checklistClass">
                    <input type="checkbox" checked id="allUni" @click="selectAllUni()">
                    <p class="checklistItem"><b>Select all institutions</b></p>
                  </div>
                  <div v-for="item in uniListFull" :key="item.shortUni" class="checklistClass">
                    <input type="checkbox" checked :id="item.shortUni" @click="changeUni()">
                    <p class="checklistItem">{{ item.longUni }}</p>
                  </div>
                </div>
              </div>
            </template>
          </FaqExpandable>

        </div>


        <div class="newsItemsRight">

          <div v-for="item in newsToDisplay" :key="item.id" class="referenceItem">
            <img class="referenceImg" :src="item.Image">
            <div>
              <p class="referenceTitle" @click="openExternalLink(item.URL)">{{ item.Title }}</p>
              <p class="referenceBlurb">{{ formatDate(item.Date) }} (<i>{{ item.Type }}</i>)</p>
            </div>
          </div>

        </div>



      </div>

      <div class="moveToMiddle"><button class="backButton" onclick="window.location.assign('./index.html')"
          type="button">Home</button>
      </div>
    </div>


  </div>
  <footer>
    <p><b>Questions, comments or ideas for this web portal? <a class="linkDarkTheme"
          href="mailto:info@solid-sustainability.org">Contact us!</a></b></p>
    <p>© Solid Sustainability 2023</p>
  </footer>
</template>

<script>
import './assets/css/main.css';
import news from './news.json';
import FaqExpandable from './components/FaqExpandable.vue';
import MenuBar from './components/MenuBar.vue'


export default {
  name: 'AppNews',
  components: {
    FaqExpandable,
    MenuBar
  },
  data() {
    return {
      newsToDisplay: news.sort(this.compareFunction),
      arrCatFull: [{ shortCat: 'news', longCat: "news" }, { shortCat: 'opinion', longCat: "opinion" }, { shortCat: 'press release', longCat: "press release" }, { shortCat: 'article', longCat: "article" }, { shortCat: 'interview', longCat: "interview" }, { shortCat: 'kamervragen', longCat: "kamervragen" }, { shortCat: 'research', longCat: "research" }, { shortCat: 'cartoon', longCat: "cartoon" }, { shortCat: 'other', longCat: "other" }],
      desiredCat: ["news", "opinion", "press release", "article", "interview", "kamervragen", "research", "cartoon", "other"],
      uniListFull: [{shortUni: "ABE", longUni: "University of Aberdeen"}, {shortUni: "BAT", longUni: "University of Bath"}, {shortUni: "BRU", longUni: "Brunel University"}, {shortUni: "BHAM", longUni: "University of Birmingham"}, {shortUni: "BRI", longUni: "University of Bristol"}, {shortUni: "CAM", longUni: "University of Cambridge"}, {shortUni: "EDI", longUni: "University of Edinburgh"}, {shortUni: "EXE", longUni: "University of Exeter"}, {shortUni: "ICL", longUni: "Imperial College London"}, {shortUni: "GLA", longUni: "University of Glasgow"}, {shortUni: "HWU", longUni: "Heriot-Watt University"}, {shortUni: "LEE", longUni: "University of Leeds"}, {shortUni: "MAN", longUni: "Manchester University"}, {shortUni: "NOT", longUni: "University of Nottingham"}, {shortUni: "OXF", longUni: "Oxford University"}, {shortUni: "QMUL", longUni: "Queen Mary University of London"}, {shortUni: "RHU", longUni: "Royal Holloway University"}, {shortUni: "TEE", longUni: "Teesside"}, {shortUni: "UCL", longUni: "University College London"}, {shortUni: "UKRI", longUni: "UK Research and Innovation"}],
      desiredUni: ["ABE", "BAT", "BRU", "BHAM", "BRI", "CAM", "EDI", "EXE", "ICL", "GLA", "HWU", "LEE", "MAN", "NOT", "OXF", "QMUL", "RHU", "TEE", "UCL", "UKRI"]    }
  },
  /* setup() {
     let newsToDisplay = news.sort(this.compareFunction)
     return {
       news
     }
   },
   computed: {
     newsSorted() {
       return this.newsToDisplay.sort(this.compareFunction)
     }
   }, */
  methods: {
    formatDate(date_a) {
      let tmp = new Date(date_a);
      //return Date(tmp).toString()
      return (tmp.getUTCDate() + " " + tmp.toLocaleString('default', { month: "long" }) + " " + tmp.getFullYear())
    },
    compareFunction(p1, p2) {
      let d1 = new Date(p1.Date);
      let d2 = new Date(p2.Date);
      return (((d1 > d2) | isNaN(d2)) ? -1 : ((d1 < d2) | isNaN(d1)) ? 1 : 0)
    },
    openExternalLink(link) {
      window.open(link, '_blank')
    },
    updateRows() {
      this.doSearchChangingData(this.dataToSort, 0, this.dataToSort.length, this.table.sortable.order, this.table.sortable.sort);
    },
    selectAllCat() {
      let tmpVal = document.getElementById("allCat").checked
      this.arrCatFull.forEach((item) => {
        document.getElementById(item.shortCat).checked = tmpVal
      })
      this.changeCat()
    },
    selectAllUni() {
      let tmpVal = document.getElementById("allUni").checked
      this.uniListFull.forEach((item) => {
        document.getElementById(item.shortUni).checked = tmpVal
      })
      this.changeUni()
    },
    changeCat() {
      this.desiredCat = []
      this.arrCatFull.forEach((item) => {
        if (document.getElementById(item.shortCat).checked) {
          this.desiredCat.push(item.longCat)
        }
      })
      this.newsToDisplay = news.filter(this.filterArrayCat)
      this.newsToDisplay = this.newsToDisplay.filter(this.filterArrayUni)
      this.newsToDisplay = this.newsToDisplay.sort(this.compareFunction)
    },
    changeUni() {
      this.desiredUni = []
      this.uniListFull.forEach((item) => {
        if (document.getElementById(item.shortUni).checked) {
          this.desiredUni.push(item.shortUni)
        }
      })
      this.newsToDisplay = news.filter(this.filterArrayCat)
      this.newsToDisplay = this.newsToDisplay.filter(this.filterArrayUni)
      this.newsToDisplay = this.newsToDisplay.sort(this.compareFunction)
    },
    filterArrayCat(item) {
      for (let i = 0; i < this.desiredCat.length; i++) {
        if (item.Type.includes(this.desiredCat[i])) {
          return 1
        }
      }
      return 0
    },
    filterArrayUni(item) {
      for (let i = 0; i < this.desiredUni.length; i++) {
        if (item.University.includes(this.desiredUni[i])) {
          return 1
        }
      }
      return 0
    },

  }

};

</script>

<style>
.extraspace {
  margin-bottom: 30px;
}

.groupHeader {
  font-size: 1.5em;
}
</style>
