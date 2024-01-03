<template>
  <div class="titlediv">
    <h1 v-if="currentBlurb.uni">How is <b>{{ currentBlurb.uni }}</b> tied to the fossil fuel industry?</h1>
    <h1 v-else>How is Dutch academia tied to the fossil fuel industry?</h1>
  </div>
  <div class="containerMain">
    <div class="map">
      <img class="mapImage" :src="require('../assets/NL.svg')">
      <img id="TUD" class="punt TUD" @click="selectUni('TUD')" :src="require('../assets/' + dots[TUD])" title="TU Delft">
      <img id="TUe" class="punt TUe" @click="selectUni('TUe')" :src="require('../assets/' + dots[TUe])" title="TU Eindhoven">
      <img id="RUG" class="punt RUG" @click="selectUni('RUG')" :src="require('../assets/' + dots[RUG])" title="Rijksuniversiteit Groningen">
      <img id="UvA" class="punt UvA" @click="selectUni('UvA')" :src="require('../assets/' + dots[UvA])" title="Universiteit van Amsterdam">
      <img id="LU" class="punt LU" @click="selectUni('LU')" :src="require('../assets/' + dots[LU])"  title="Universiteit Leiden">
      <img id="WUR" class="punt WUR" @click="selectUni('WUR')" :src="require('../assets/' + dots[WUR])"  title="Wageningen University & Research">
      <img id="EUR" class="punt EUR" @click="selectUni('EUR')" :src="require('../assets/' + dots[EUR])"  title="Erasmus Universiteit Rotterdam">
      <img id="UM" class="punt UM" @click="selectUni('UM')" :src="require('../assets/' + dots[UM])"  title="Maastricht University">
      <img id="RUN" class="punt RUN" @click="selectUni('RUN')" :src="require('../assets/' + dots[RUN])"  title="Radboud Universiteit (Nijmegen)">
      <img id="UU" class="punt UU" @click="selectUni('UU')" :src="require('../assets/' + dots[UU])"  title="Universiteit Utrecht">
      <img id="UT" class="punt UT" @click="selectUni('UT')" :src="require('../assets/' + dots[UT])"  title="Universiteit Twente">
      <img id="VU" class="punt VU" @click="selectUni('VU')" :src="require('../assets/' + dots[VU])"  title="VU Amsterdam">
      <img id="Til" class="punt Til" @click="selectUni('Til')" :src="require('../assets/' + dots[Til])"  title="Tilburg University">
      <img id="OU" class="punt OU" @click="selectUni('OU')" :src="require('../assets/' + dots[OU])"  title="Open Universiteit">
      <img id="NWO" class="punt NWO" @click="selectUni('NWO')" :src="require('../assets/' + dots[NWO])" title="NWO (funding body)">
    </div>
    <div class="map">
      <div class="blurb">

        <h3 v-if="currentBlurb.uni">{{ currentBlurb.uni }} - <a @click="clickToSelectUni()">Go to database of ties</a></h3>
      <ShortSummary :blurb="currentBlurb" />
    <button v-if="(currentBlurb.uni) && (currentBlurb.shortForm != 'NWO')" @click="clickToSelectUni()">
      <b>See database of ties for {{ currentBlurb.uni }}</b>
    </button>
    </div>
    </div>
  </div>
</template>

<script>
import blurbs from '../blurb.json';
import ShortSummary from "./ShortSummary.vue"


export default {
  name: 'InteractiveMap',
  components: {
    ShortSummary
  },
  props: {
    msg: String
  },
  emits: ["select-uni"],
  data() {
    return {
      dots: ['smalldot.svg', 'bigdot.svg'],
      UvA: 0,
      TUD: 0,
      TUe: 0,
      RUG: 0,
      LU: 0,
      UM: 0,
      RUN: 0,
      NWO: 0,
      OU: 0,
      EUR: 0,
      Til: 0,
      UT: 0,
      UU: 0,
      VU: 0,
      WUR: 0,
      prevSelected: "TUD",
      currentBlurb: {
        "shortForm": "nuthin",
        "uni": ""
      },
      blurbs: blurbs
    }
  },
  methods: {
    selectUni(uni) {
      eval('this.' + this.prevSelected + '= 0')
      eval('this.' + uni + '= 1')
      if (uni != this.prevSelected) {
        document.getElementById(uni).style.zIndex = "1"
        document.getElementById(this.prevSelected).style.zIndex = "2"
      }
      this.prevSelected = uni
      this.getSlideFromID(uni)
      localStorage.setItem("shortUni", this.currentBlurb.shortForm)
      localStorage.setItem("nameUni", this.currentBlurb.uni)
    },
    getSlideFromID(newID) {
      //TODO: change chapter if new chapter
      this.currentBlurb = this.blurbs.filter(element => element.shortForm == newID)[0]
      // TODO: add error handler if next slide does not exist. (e.g. go to start or page not found)
      if (!(this.currentBlurb)) {
        console.log("could not find uni")
      }
    },
    clickToSelectUni() {
      this.$emit("select-uni", this.currentBlurb)
      window.location.assign('./Database.html')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mapImage {
  max-height: calc(100vh - 168px);
  max-width: min(calc(100vw - 30px), 600px);
 /* margin-left: 10px;
  margin-right: 20px; */
  padding: 0pt;
  z-index: 0;
  position: relative;
  left: 0;
}

.map {
  position: relative;
  margin-left: auto;
  margin-right: auto;
  width: fit-content;
  padding: 0pt;
  flex: content;
}

.blurb {

  margin: 20px 10px ;
  padding: 0;
  align-content: center;
  text-align: center;
}

.punt {
  width: 5%;
  z-index: 2;
  position: absolute;
  cursor: pointer;
}

.TUD {
  left: 29.5%;
  top: 52.5%;
}

.NWO {
  left: 27%;
  top: 50%;
}

.TUe {
  left: 54%;
  top: 72%;
}

.Til {
  left: 44%;
  top: 67%;
}

.OU {
  left: 65%;
  top: 90.5%;
}

.RUG {
  left: 80%;
  top: 10%;
}

.UvA {
  left: 40.5%;
  top: 39.5%;
}

.LU {
  left: 32.5%;
  top: 47%;
}

.WUR {
  left: 57%;
  top: 53%;
}

.EUR {
  left: 33%;
  top: 56%;
}

.UU {
  left: 46%;
  top: 49%;
}

.UT {
  left: 84%;
  top: 45%;
}

.VU {
  left: 39.5%;
  top: 41%;
}

.RUN {
  left: 61%;
  top: 59%;
}

.UM {
  left: 58.5%;
  top: 93%;
}
</style>
