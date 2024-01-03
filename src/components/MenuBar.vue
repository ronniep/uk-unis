<template>
  <div v-if="this.width > 610" class="menubar">
    <div class="innermenubar">
      <a class="naviLink" href="index.html">Home</a>
      <a class="naviLink" href="Database.html">Database</a>
      <a class="naviLink" href="FAQ.html">FAQs</a>
      <a class="naviLink" href="News.html">News</a>
      <a class="naviLink" href="About.html">About and Contact</a>
    </div>
  </div>
  <div v-else>
    <header @click="toggle" class="menubar menubarsmall">
      <div>Menu <img class="arrow" width="16" :src="require('../assets/' + image + '.png')"> </div>
    </header>
    <div class="menubarlinksmenu" :style="displayStyle">
      <div class="makestickto">
        <div class="naviLinkContain"><a class="naviLinkSmall" href="index.html">Home</a></div>
        <div class="naviLinkContain"><a class="naviLinkSmall" href="Database.html">Database</a></div>
        <div class="naviLinkContain"><a class="naviLinkSmall" href="FAQ.html">FAQs</a></div>
        <div class="naviLinkContain"><a class="naviLinkSmall" href="News.html">News</a></div>
        <div class="naviLinkContain"><a class="naviLinkSmall" href="About.html">About and Contact</a></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuBar',
  data() {
    return {
      width: document.documentElement.clientWidth,
      open: false,
      image: "arrowlinedown"
    }
  },
  methods: {
    changeClass() {
      this.width = document.documentElement.clientWidth;
    },
    toggle() {
      this.open = !(this.open)
      if (this.open) {
        this.image = "arrowlineup"
      } else {
        this.image = "arrowlinedown"
      }
    }
  },
  computed: {
    displayStyle() {
      return this.open ? "display: block" : "display: none"
    }
  },
  mounted() {
    window.addEventListener('resize', this.changeClass);
  },
}
</script>


<style>
h2 {
  margin: 10px 0px;
  font-size: larger;
  text-align: left;
}

.arrow {
  margin-right: 8px;
  margin-left: 8px;
  margin-bottom: -2px;
  margin-top: 2px;
}
</style>