<template>
  <div class="house">
      <div class="titlediv">
        <h1>{{ Title }}</h1>
      </div>



      <div id="profile" class="bodydiv">
        <h3>What relationships with fossil fuel companies are known so far:</h3>
        
        <h3><b>Please note! This database is a work in progress and not yet publicly launched! There may be inaccuracies in the data.</b>
  </h3>
      <FaqExpandable>
        <template #header>
          Filter by type of relationship
        </template>
        <template #default>
          <div class="checklistClass">
          <input type="checkbox" checked id="allCat" @click="selectAllCat()">
            <p class="checklistItem"><b>Select all categories</b></p>
          </div>
          <div v-for="item in arrCatFull" :key="item.shortCat" class="checklistClass">
            <input type="checkbox" checked :id="item.shortCat" @click="changeCat()">
            <p class="checklistItem">{{ item.longCat }}</p>
          </div>
        </template>
      </FaqExpandable>

      <FaqExpandable v-if="!this.UniShort">
        <template #header>
          Filter by institution
        </template>
        <template #default>
          <div class="checklistClass">
          <input type="checkbox" checked id="allUni" @click="selectAllUni()">
            <p class="checklistItem"><b>Select all institutions</b></p>
          </div>
          <div v-for="item in uniListFull" :key="item.shortUni" class="checklistClass">
            <input type="checkbox" checked :id="item.shortUni" @click="changeUni()">
            <p class="checklistItem">{{ item.shortUni }} ({{ item.longUni }})</p>
          </div>
        </template>
      </FaqExpandable>

        <table-lite :is-fixed-first-column="false" :max-height="500" :is-loading="table.isLoading"
          :columns="table.columns" :rows="table.rows" :total="table.totalRecordCount" :sortable="table.sortable"
          :messages="table.messages" @do-search="doSearch" :page-options="table.pageOptions"
          @is-finished="table.isLoading = false"></table-lite>
      </div>

    <div class="bodydiv">


      <button v-if="this.UniShort" class="backButton " @click="goToFullDatabase()" type="button">Go to Database for All Universities</button>


      <button class="backButton " onclick="window.location.assign('./index.html')" type="button">Back to Home</button>

    </div>
  </div>
</template>

<script>
import '../assets/css/main.css';
import { reactive } from "vue";
import TableLite from "vue3-table-lite"
import data from '../assets/ties.json';
import FaqExpandable from './FaqExpandable.vue';


//let arrCat = ["(Co-)funding/supporting research (money or in kind)", "Influence on research publication, patents, or results (including hindering publication)", "Memorandum of Understanding (MoU) or other agreement", "Staff/board members with additional (advisory) role for fossil(-related) company", "Externally (partially-)financed research chair", "Sponsoring students' studies e.g. via bursaries or prizes", "Sponsoring student activities or organisations", "Career event", "Exclusive job/internship opportunities", "Guest lecture, talk or other influence on programme of study", "Discussion panels and talks not associated with a programme of study", "Alumni Network/other network", "Other form of relationship"]





export default {
  name: 'UniData',
  components: {
    TableLite,
    FaqExpandable
  },
  data() {
    return {
      dataToDisplay: [],
      arrCatFull: [{ shortCat: 'funding', longCat: "(Co-)funding/supporting research (money or in kind)" }, { shortCat: 'influence', longCat: "Influence on research publication, patents, or results (including hindering publication)" }, { shortCat: 'mou', longCat: "Memorandum of Understanding (MoU) or other agreement" }, { shortCat: 'staff', longCat: "Staff/board members with additional (advisory) role for fossil(-related) company/organisation" }, { shortCat: 'chair', longCat: "Externally (partially-)financed research chair" }, { shortCat: 'bursary', longCat: "Sponsoring students' studies e.g. via bursaries or prizes" }, { shortCat: 'sponsor', longCat: "Sponsoring student or outreach activities or organisations" }, { shortCat: 'career', longCat: "Career event" }, { shortCat: 'job', longCat: "Exclusive job/internship opportunities" }, { shortCat: 'study', longCat: "Guest lecture, talk or other influence on programme of study" }, { shortCat: 'talk', longCat: "Discussion panels and talks not associated with a programme of study" }, { shortCat: 'alumni', longCat: "Alumni Network/other network" }, { shortCat: 'other', longCat: "Other form of relationship" }],
      desiredCat: ["(Co-)funding/supporting research (money or in kind)" , "Influence on research publication, patents, or results (including hindering publication)", "Memorandum of Understanding (MoU) or other agreement" , "Staff/board members with additional (advisory) role for fossil(-related) company/organisation" , "Externally (partially-)financed research chair", "Sponsoring students' studies e.g. via bursaries or prizes" , "Sponsoring student or outreach activities or organisations" , "Career event" , "Exclusive job/internship opportunities" ,  "Guest lecture, talk or other influence on programme of study" ,  "Discussion panels and talks not associated with a programme of study" , "Alumni Network/other network" , "Other form of relationship"],
      uniListFull: [{shortUni: "ABE", longUni: "University of Aberdeen"}, {shortUni: "BAT", longUni: "University of Bath"}, {shortUni: "BRU", longUni: "Brunel University"}, {shortUni: "BHAM", longUni: "University of Birmingham"}, {shortUni: "BRI", longUni: "University of Bristol"}, {shortUni: "CAM", longUni: "University of Cambridge"}, {shortUni: "EDI", longUni: "University of Edinburgh"}, {shortUni: "EXE", longUni: "University of Exeter"}, {shortUni: "ICL", longUni: "Imperial College London"}, {shortUni: "GLA", longUni: "University of Glasgow"}, {shortUni: "HWU", longUni: "Heriot-Watt University"}, {shortUni: "LEE", longUni: "University of Leeds"}, {shortUni: "MAN", longUni: "Manchester University"}, {shortUni: "NOT", longUni: "University of Nottingham"}, {shortUni: "OXF", longUni: "Oxford University"}, {shortUni: "QMUL", longUni: "Queen Mary University of London"}, {shortUni: "RHU", longUni: "Royal Holloway University"}, {shortUni: "TEE", longUni: "Teesside"}, {shortUni: "UCL", longUni: "University College London"}, {shortUni: "UKRI", longUni: "UK Research and Innovation"}],
      desiredUni: ["ABE", "BAT", "BRU", "BHAM", "BRI", "CAM", "EDI", "EXE", "ICL", "GLA", "HWU", "LEE", "MAN", "NOT", "OXF", "QMUL", "RHU", "TEE", "UCL", "UKRI"]    }
  },
  props: {
    UniShort: String,
    UniName: String,
  },
  methods: {
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
      this.dataToSort = this.dataFiltered.filter(this.filterArrayCat)
      this.dataToSort = this.dataToSort.filter(this.filterArrayUni)
      this.updateRows()
    },
    changeUni() {
      this.desiredUni = []
      this.uniListFull.forEach((item) => {
        if (document.getElementById(item.shortUni).checked) {
          this.desiredUni.push(item.shortUni)
        }
      })
      this.dataToSort = this.dataFiltered.filter(this.filterArrayCat)
      this.dataToSort = this.dataToSort.filter(this.filterArrayUni)
      this.updateRows()
    },
    filterArrayCat(item) {
      for (let i = 0; i < this.desiredCat.length; i++) {
        if (item.typeLong.includes(this.desiredCat[i])) {
          return 1
        }
      }
      return 0
    },
    filterArrayUni(item) {
      for (let i = 0; i < this.desiredUni.length; i++) {
        if (item.uni.includes(this.desiredUni[i])) {
          return 1
        }
      }
      return 0
    }, 
    goToFullDatabase() {
      localStorage.removeItem("shortUni")
      localStorage.removeItem("nameUni")
      location.reload()
    }
  },
  computed: {
    Title() {
      return this.UniName ? this.UniName : "All Institutions"

    }
  },
  mounted() {
    this.doSearch(0, this.table.pageOptions[0].value, this.table.sortable.order, this.table.sortable.sort);
  },
  setup() {
    let uniShortForm = ""
    try {
      uniShortForm = localStorage.getItem("shortUni")
    }
    catch (error) {
      console.log("displaying whole database")
    }
    let dataChecked = data.filter(element => (element.checked == "1"))
    let dataFiltered = []
    if (uniShortForm) {
      dataFiltered = dataChecked.filter(element => element.uni.includes(uniShortForm))
    }
    else {
      dataFiltered = dataChecked
    }
    for (let i = 0; i < dataFiltered.length; i++) {

      // decode date start to unicode
      try {
        dataFiltered[i].date_start_UTC = Date.parse(dataFiltered[i].date_start)
      }
      catch (error) {
        dataFiltered[i].date_start_UTC = 0
      }

      if (isNaN(dataFiltered[i].date_start_UTC)) { dataFiltered[i].date_start_UTC = 0 }

      if (dataFiltered[i].date_end == "to date") {
        dataFiltered[i].date_end_UTC = Date.now()
        if (dataFiltered[i].date_start_UTC == 0) {
          dataFiltered[i].date_start_UTC = dataFiltered[i].date_end_UTC
        }
      }
      else {

        try {
          dataFiltered[i].date_end_UTC = Date.parse(dataFiltered[i].date_end)
        }
        catch (error) {
          dataFiltered[i].date_end_UTC = dataFiltered[i].date_start_UTC
        }
      }

      if (isNaN(dataFiltered[i].date_end_UTC)) { dataFiltered[i].date_end_UTC = dataFiltered[i].date_start_UTC }

      // decode types to long description
      let typesArr = dataFiltered[i].type.split(',') // splits along , in case more than one
      for (let j = 0; j < typesArr.length; j++) {
        if (j == 0) {
          dataFiltered[i].typeLong = ""
        }
        else {
          dataFiltered[i].typeLong += ", "
        }
        switch (typesArr[j].replace(/\s+/g, '')) {  // removes spaces
          case 'funding':
            dataFiltered[i].typeLong += "(Co-)funding/supporting research (money or in kind)"
            break
          case 'influence':
            dataFiltered[i].typeLong += "Influence on research publication, patents, or results (including hindering publication)"
            break
          case 'mou':
            dataFiltered[i].typeLong += "Memorandum of Understanding (MoU) or other agreement"
            break
          case 'staff':
            dataFiltered[i].typeLong += "Staff/board members with additional (advisory) role for fossil(-related) company/organisation"
            break
          case 'chair':
            dataFiltered[i].typeLong += "Externally (partially-)financed research chair"
            break
          case 'bursary':
            dataFiltered[i].typeLong += "Sponsoring students' studies e.g. via bursaries or prizes"
            break
          case 'sponsor':
            dataFiltered[i].typeLong += "Sponsoring student or outreach activities or organisations"
            break
          case 'career':
            dataFiltered[i].typeLong += "Career event"
            break
          case 'job':
            dataFiltered[i].typeLong += "Exclusive job/internship opportunities"
            break
          case 'study':
            dataFiltered[i].typeLong += "Guest lecture, talk or other influence on programme of study"
            break
          case 'talk':
            dataFiltered[i].typeLong += "Discussion panels and talks not associated with a programme of study"
            break
          case 'alumni':
            dataFiltered[i].typeLong += "Alumni Network/other network"
            break
          case 'other':
            dataFiltered[i].typeLong += "Other form of relationship"
            break
        }

      }
    }

    let columnsVar = [
      {
        label: "Description",
        field: "description",
        width: "40%",
        //sortable: true,
      },
      {
        label: "Type of relationship",
        field: "typeLong",
        width: "15%",
        sortable: true,
        //isKey: true,
      },
      {
        label: "Companies",
        field: "third_party",
        width: "10%",
        sortable: true,
      },
      {
        label: "Amount",
        field: "project_size",
        width: "10%",
        sortable: true,
      },
      {
        label: "Date begin",
        field: "date_start",
        width: "7%",
        sortable: true,
      },
      {
        label: "Date end",
        field: "date_end",
        width: "7%",
        sortable: true,
      },
      {
        label: "Links",
        field: "URL1",
        width: "10%",
        display: function (row) {
          let str = ""
          if (row.URL1) {
            str += '<a href="' + row.URL1 + '" target="_blank">Link 1</a>'
          }
          if (row.URL2) {
            str += ', <a href="' + row.URL2 + '" target="_blank">Link 2</a>'
          }
          if (row.URL3) {
            str += ', <a href="' + row.URL3 + '" target="_blank">Link 3</a>'
          }
          if (row.URL4) {
            str += ', <a href="' + row.URL4 + '" target="_blank">Link 4</a>'
          }
          if (row.URL5) {
            str += ', <a href="' + row.URL5 + '" target="_blank">Link 5</a>'
          }
          return str
        },
      },
    ]

    if (!uniShortForm) {
      columnsVar.splice(2, 0,
        {
          label: "Institutions",
          field: "uni",
          width: "5%",
          sortable: true,
        })
    }

    let dataToSort = dataFiltered.slice();

    // Table config
    const table = reactive({
      isLoading: false,
      columns: columnsVar,
      rows: [],
      totalRecordCount: 0,
      sortable: {
        order: "date_start",
        sort: "desc",
      },
      pageOptions: [
        {
          value: 10,
          text: 10
        },
        {
          value: 50,
          text: 50
        },
        {
          value: 1000,
          text: 'all'
        }
      ]
    });
    /**
     * Search Event
     */



    const sortData = (data, field, sort) => {

      let sortField = field

      switch (field) {
        case 'date_start': {
          sortField = 'date_start_UTC'
          break
        }
        case 'date_end': {
          sortField = 'date_end_UTC'
          break
        }
      }

      if (sort == 'asc') {

        for (let i = 1; i < data.length; i++) {
          let j = i;
          let whileCondition = (j > 0) & (data[j][sortField] < data[j - 1][sortField])
          while (whileCondition) {
            let temp = data[j];
            data[j] = data[j - 1];
            data[j - 1] = temp;
            j--;

            if (j > 0) {
              whileCondition = (data[j][sortField] < data[j - 1][sortField])
            }
            else {
              whileCondition = 0
            }
          }
        }
      }
      else {

        for (let i = 1; i < data.length; i++) {
          let j = i;
          let whileCondition = (j > 0) & (data[j][sortField] > data[j - 1][sortField])
          while (whileCondition) {
            let temp = data[j];
            data[j] = data[j - 1];
            data[j - 1] = temp;
            j--;
            if (j > 0) {
              whileCondition = (data[j][sortField] > data[j - 1][sortField])
            }
            else {
              whileCondition = 0
            }
          }
        }
      }

    }


    const doSearch = (offset, limit, order, sort) => {
      table.isLoading = false;
      setTimeout(() => {
        // do sorting
        // If calling doSearch because you resorted
        //if (!((table.sortable.order == order) & (table.sortable.sort == sort))) {
        sortData(dataToSort, order, sort)
        //}
        // table.rows = dataFiltered //sampleData1(offset, limit);
        // set values

        table.isReSearch = offset == undefined ? true : false;
        /*if (offset >= 50 || limit >= 100) {
          limit = dataFiltered.length;
        }*/ // no idea waht this does

        // only display between offset and offset + 10 (or whatever your page length is)
        table.rows = dataToSort.slice(offset, Math.min((offset + limit), dataToSort.length)) //sampleData1(offset, limit);
        // TODO: replace 10 with currently selected page size, find this out.

        table.totalRecordCount = dataToSort.length;
        table.sortable.order = order;
        table.sortable.sort = sort;
      }, 600);
    };



    const doSearchChangingData = (data, offset, limit, order, sort) => {
      dataToSort = data;
      doSearch(offset, limit, order, sort)
    };



    // First get data
    return {
      table,
      doSearch,
      doSearchChangingData,
      dataFiltered,
      dataToSort
    };
  },
};

</script>

