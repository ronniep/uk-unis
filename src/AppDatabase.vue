<template>
  <div class="house">
    <div class="midcontainer">
    <MenuBar />
    </div>
    <div>
      <UniData :UniShort="this.shortUni" :UniName="this.nameUni" />
    </div>
  </div>
<footer>
  <p><b>Questions, comments or ideas for this web portal? <a class="linkDarkTheme"
        href="mailto:info@solid-sustainability.org">Contact us!</a></b></p>
  <p>© Solid Sustainability 2023</p>
</footer>

</template>

<script>
import UniData from "./components/UniData.vue"
import MenuBar from "./components/MenuBar.vue"
import './assets/css/main.css';

export default {
  name: 'AppDatabase',
  components: {
    UniData,
    MenuBar
  },
  data() {
    return {
      uniNonSelected: true,
      shortUni: String,
      nameUni: String
    }
  },
  methods: {
    selectUni(uni) {
      this.shortUni = uni.shortForm
      this.nameUni = uni.uni
      this.uniNonSelected = false
    },
    deselectUni() {
      this.uniNonSelected = true
    }
  },
  mounted () {
    this.shortUni = localStorage.getItem("shortUni")
    this.nameUni = localStorage.getItem("nameUni")
  }
}
</script>
