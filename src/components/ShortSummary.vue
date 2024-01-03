<template>
  <div v-if="(blurb.uni) && (blurb.shortForm != 'NWO')"  class="parentContainer">
    <div :class="classVariable">

      <h3>External professorships</h3>
      <div class="subsection splitFossilTrans">
        <div class="subsection">
          <img :src="require('../assets/icons/' + profsImgTrans + '.png')" class="icon">
        </div>
        <div class="subsectiondescription">
          <p v-if="this.blurb.Extern_profs_published == 2">A <a :href="this.blurb.Extern_profs_link"
              target="_blank">list</a> of externally-funded research chairs is updated {{
                blurb.Extern_profs_update }}.
          </p>
          <p v-else-if="this.blurb.Extern_profs_published == 1">A <a :href="this.blurb.Extern_profs_link"
              target="_blank">list</a> of externally-funded research chairs has
            been published but it is not known how often it is updated.
          </p>
          <p v-else-if="this.blurb.Extern_profs_published == 0">No complete list of externally-funded research chairs
            (including part-time professors with an additional appointment elsewhere) has been published.
          </p>
          <p v-else>
            It is not known if a list of externally-funded research chairs has been published.
          </p>
        </div>
      </div>
      <div class="subsection splitFossilTrans">

        <div class=" subsection">
          <img :src="require('../assets/icons/' + profsImgFossil + '.png')" class="icon">
        </div>
        <div class="subsectiondescription">
          <p v-if="this.blurb.Extern_profs_fossil == null">
            It is not known if any professors are paid by fossil companies.
          </p>
          <p v-else-if="this.blurb.Extern_profs_fossil == 1">
            1 professor is funded by, or has an position at, a fossil company/organisation.
          </p>
          <p v-else>
            {{ this.blurb.Extern_profs_fossil }} professors are funded by, or have an position at, a fossil
            company/organisation.
          </p>
        </div>
      </div>


      <h3>Third-party funding</h3>
      <div class="subsection splitFossilTrans">
        <div class="subsection">
          <img :src="require('../assets/icons/' + moneyImgTrans + '.png')" class="icon">
        </div>

        <div class="subsectiondescription">

          <p>

            <span v-if="this.blurb.Third_party_funds_amount_published == 2">The amount of <a
                v-if="this.blurb.Third_party_funds_link" :href="this.blurb.Third_party_funds_link"
                target="_blank">third-party funding</a><span v-else>third-party funding</span> is updated
              {{
                blurb.Third_party_funds_updated }}.
            </span>
            <span v-else-if="this.blurb.Third_party_funds_amount_published == 1">The amount of <a
                v-if="this.blurb.Third_party_funds_link" :href="this.blurb.Third_party_funds_link"
                target="_blank">third-party funding</a><span v-else>third-party funding</span>
              is not regularly published.
            </span>
            <span v-else-if="this.blurb.Third_party_funds_amount_published === 0">The amount of third-party funding
              is not published.
            </span>
            <span v-else>
              It is not known if the amount of third-party funding is published.
            </span>

            <span v-if="(this.blurb.Third_party_funds_breakdown_published == '1') | (this.blurb.Third_party_funds_breakdown_published == '2')">
              The university has <a :href="this.blurb.Collab_list_link"
                target="_blank">published</a> a {{ this.blurb.Third_party_funds_notes }}.
            </span>
            <span v-else>
              It is not specified which companies provide financing.
            </span>




          </p>



        </div>
      </div>
      <div class="subsection splitFossilTrans">

        <div class=" subsection">
          <img :src="require('../assets/icons/' + moneyImgFossil + '.png')" class="icon">
        </div>
        <div class="subsectiondescription">
          <p v-if="this.blurb.Third_party_funds_fossil">
            Fossil funding accounts for {{ this.blurb.Third_party_funds_fossil }}. <a :href="this.blurb.Collab_amount_link" target="_blank" v-if="this.blurb.Collab_amount_link">Read more</a>
          </p>
          <p v-else>
            It is not known how much of this funding is from fossil companies.
          </p>
        </div>
      </div>

      <h3>Careers fairs</h3>
      <div class="subsection">
        <div class="subsection">
          <img :src="require('../assets/icons/' + fairImg + '.png')" class="icon">
        </div>
        <div class="subsectiondescription">
          <p v-if="this.blurb.Careers_fairs == 'yes'">Fossil companies <a v-if="this.blurb.Careers_fairs_link"
              :href="this.blurb.Careers_fairs_link" target="_blank">are present</a><span v-else>are present</span> at
            careers fairs.
          </p>
          <p v-else-if="this.blurb.Careers_fairs == 'no'">Careers fairs are fossil-free.
          </p>
          <p v-else>
            It is not known if fossil companies are present at careers fairs.
          </p>
        </div>
      </div>





      <h3>Policies</h3>
      <div class="subsection splitFossilTrans">
        <div class="subsection">
          <img :src="require('../assets/icons/' + policyImgSus + '.png')" class="icon">
        </div>
        <div class="subsectiondescription">
          <p v-if="(this.blurb.policy_sustainability_is == 'yes') & (this.blurb.climate_emergency)">The university has a
            sustainability policy, to be found
            <a :href="this.blurb.policy_sustainability_link" target="_blank">here</a>. The university has <a
              :href="this.blurb.climate_emergency_link" target="_blank">declared climate emergency</a>.
          </p>
          <p v-else-if="this.blurb.policy_sustainability_is == 'yes'">
            The university has a sustainability policy, to be found
            <a :href="this.blurb.policy_sustainability_link" target="_blank">here</a>.
          </p>
          <p v-else-if="this.blurb.policy_sustainability_is == 'no'">The university has no known sustainability policy.
          </p>
          <p v-else>
            It is not known if the university has a sustainability policy.
          </p>
        </div>
      </div>
      <div class="subsection splitFossilTrans">
        <div class=" subsection">
          <img :src="require('../assets/icons/' + policyImgFossil + '.png')" class="icon">
        </div>
        <div class="subsectiondescription">
          <p v-if="this.blurb.policy_specific_is == 'none'">The university has no known official policy for working with
            fossil
            companies.
          </p>
          <p v-else-if="(this.blurb.policy_specific_is == null) | (this.blurb.policy_specific_is == '')">
            It is not known if there is a policy for working with fossil companies.
          </p>
          <p v-else>
            {{ blurb.policy_specific_is }} <span v-if="blurb.policy_specific_link"><a :href="blurb.policy_specific_link" target="_blank">Read more</a></span> 
          </p>
        </div>
      </div>


      <h3>Democratic discussion</h3>
      <div class="subsection">
        <div class="subsection">
          <img :src="require('../assets/icons/' + convoImg + '.png')" class="icon">
        </div>
        <div class="subsectiondescription">
          <p v-if="this.blurb.ties_discussion == 3">The university administration has started a
            discussion about fossil ties open to students and staff, which will influence university policy on fossil
            ties. <a v-if="this.blurb.ties_discussion_link != ''" :href="this.blurb.ties_discussion_link"
              target="_blank">Read more</a>
          </p>
          <p v-else-if="this.blurb.ties_discussion == 2">The university administration has started a
            discussion about fossil ties open to students and staff, however, it is not clear if this will influence
            university policy on fossil ties. <a v-if="this.blurb.ties_discussion_link != ''"
              :href="this.blurb.ties_discussion_link" target="_blank">Read more</a>
          </p>
          <p v-else-if="this.blurb.ties_discussion == 1">The university administration has started an internal discussion
            about fossil ties, but this is not fully open to students and staff.
          </p>
          <p v-else-if="this.blurb.ties_discussion === 0">The university administration has not started a university-wide
            discussion about fossil ties.
          </p>
          <p v-else>
            It is not known if the university administration has started a discussion about fossil ties.
          </p>
        </div>
      </div>

      <div v-if="actionGroupImg">
        <h3>Groups campaigning on fossil ties:</h3>
        <div v-for="item in activistGroupList" :key="item.name" class="subsection">
          <img :src="require('../assets/logo_thumbs/' + item.img)" class="icon">
          <div class="subsectiondescription">
            <a :href="item.link" target="_blank">{{ item.name }}</a>
          </div>
        </div>
      </div>


      <!--

      <div v-if="mediaImg" class="subsection">
        <img :src="require('../assets/icons/news.png')" class="icon">
        <div class="subsectiondescription">
          <p v-if="(this.blurb.media_local) & (this.blurb.media_uni)">There has been reporting on the fossil ties of {{ blurb.uni }} in external and campus media.</p>
          <p v-else-if="this.blurb.media_local">There has been reporting on the fossil ties of {{ blurb.uni }} in external media.</p>
          <p v-else>There has been reporting on the fossil ties of {{ blurb.uni }} in campus media</p>
        </div>
      </div>
-->



      <div v-if="progressImg" class="subsection">
        <img :src="require('../assets/icons/progress.png')" class="icon">
        <div class="subsectiondescription">
          <p v-html="this.blurb.progress"></p>
        </div>
      </div>


    </div>

    <div class="moveToMiddle disclaimer">We endeavour to keep this overview up to date, however if you have any new
      information, please contact us.</div>


    <!--   
    <div :class="legend">
        <h3>Legend</h3>
      <div class="subsectionLegend">
        <div class="legendItem">
        <img :src="require('../assets/icons/blue.png')" class="iconLegend">
        <div class="subsectiondescription">
          <p>Transparent (and fossil-free, if applicable)</p>
        </div>
      </div>
      <div class="legendItem">
        <img :src="require('../assets/icons/bluegrey.png')" class="iconLegend">
        <div class="subsectiondescription">
          <p>Semi-transparent</p>
        </div>
      </div>
      <div class="legendItem">
                <img :src="require('../assets/icons/grey.png')" class="iconLegend">
        <div class="subsectiondescription">
          <p>Intransparent or unknown</p>
        </div>
      </div>
      <div class="legendItem">
                <img :src="require('../assets/icons/yellow.png')" class="iconLegend">
        <div class="subsectiondescription">
          <p>Fossil ties</p>
        </div>
      </div>
      <div class="legendItem">
                <img :src="require('../assets/icons/blueyellow.png')" class="iconLegend">
        <div class="subsectiondescription">
          <p>(Semi-)transparent, but with fossil ties</p>
        </div>
      </div>
      <div class="legendItem">
                <img :src="require('../assets/icons/greyyellow.png')" class="iconLegend">
        <div class="subsectiondescription">
          <p>Intransparent, but with fossil ties</p>
        </div>
        </div>
      </div>
    </div>
  -->
  </div>
  <h3 v-else-if="this.blurb.shortForm=='NWO'">Select another institution to find out more</h3>
  <h3 v-else>Select an institution to find out more</h3>
</template>

<script>

export default {
  name: 'ShortSummary',
  props: {
    blurb: {
      type: Object,
      default() {
        return {
          "shortForm": "nuin",
          "uni": ""
        }
      }
    }
  },
  data() {
    return {
      width: document.documentElement.clientWidth
    }
  },
  mounted() {
    window.addEventListener('resize', this.changeClass);
  },
  computed: {
    profsImgTrans() {
      try {
        if (this.blurb.Extern_profs_published == 2) {
          return "transparent"
        }
        else if (this.blurb.Extern_profs_published == 1) {
          return "transparent"
        }
        else if (this.blurb.Extern_profs_published == 0) {
          return "intransparent"
        }
        else {
          return "unknown-transparent"
        }
      }
      catch {
        return "unknown-transparent"
      }
    },
    profsImgFossil() {
      try {
        if (this.blurb.Extern_profs_fossil == 0) {
          return "fossil-free"
        }
        else if (this.blurb.Extern_profs_fossil) {
          return "fossil-ties"
        }
        else {
          return "unknown-fossil"
        }
      }
      catch {
        return "unknown-fossil"
      }
    },
    fairImg() {
      try {
        if (this.blurb.Careers_fairs == "no") {
          return "fossil-free"
        }
        else if (this.blurb.Careers_fairs == "yes") {
          return "fossil-ties"
        }
        else {
          return "unknown-fossil"
        }
      }
      catch {
        return "unknown-fossil"
      }
    },
    policyImgSus() {
      try {
        if (this.blurb.policy_sustainability_is == "no") {
          return "no-sustainability-policy"
        }
        else if (this.blurb.policy_sustainability_is == "yes") {
          return "sustainability-policy"
        }
        else {
          return "unknown"
        }
      }
      catch {
        return "unknown"
      }
    },
    policyImgFossil() {
      try {
        if (this.blurb.policy_complete) {
          return "no-fossil-policy"
        }
        else {
          return "no-no-fossil-policy"
        }
      }
      catch {
        return "unknown"
      }
    },
    moneyImgTrans() {
      try {
        if (this.blurb.Third_party_funds_breakdown_published) {
          return "transparent"
        }
        else if (this.blurb.Third_party_funds_amount_published) {
          return "intransparent"
        }
        else {
          return "unknown-transparent"
        }
      }
      catch {
        return "unknown-transparent"
      }
    },
    moneyImgFossil() {
      try {
        if (this.blurb.Third_party_funds_fossil === 0) {
          return "fossil-free"
        }
        else if (this.blurb.Third_party_funds_fossil) {
          return "fossil-ties"
        }
        else {
          return "unknown-fossil"
        }
      }
      catch {
        return "unknown-fossil"
      }
    },
    convoImg() {
      try {
        if (this.blurb.ties_discussion == 3) {
          return "democratic-discussion"
        }
        else if ((this.blurb.ties_discussion == 1) | (this.blurb.ties_discussion == 2)) {
          return "discussion"
        }
        else {
          return "no-discussion"
        }
      }
      catch {
        return "unknown"
      }
    },
    classVariable() {
      if (this.width < 610) {
        return "smallBlurb"
      }
      else {
        return "largeBlurb"
      }
    },
    legend() {
      if (this.width < 610) {
        return "legendSmall"
      }
      else {
        return "legendLarge"
      }
    },
    actionGroupImg() {
      try {
        if (this.blurb.action_group_names) {
          return "activist"
        }
        else {
          return ""
        }
      }
      catch {
        return ""
      }
    },
    mediaImg() {
      try {
        if (this.blurb.media_local | this.blurb.media_uni) {
          return "news"
        }
        else {
          return ""
        }
      }
      catch {
        return ""
      }
    },
    progressImg() {
      try {
        if (this.blurb.progress) {
          return "progress"
        }
        else {
          return ""
        }
      }
      catch {
        return ""
      }
    },
    activistGroupList() {
      try {
        let tmpArray = []
        let names = this.blurb.action_group_names.split(',')
        let links = this.blurb.action_group_links.split(',')
        let imgs = this.blurb.action_group_img.split(',')
        for (let i = 0; i < names.length; i++) {
          tmpArray.push({ name: names[i].trim(), link: links[i].trim(), img: imgs[i].trim() })

        }
        return tmpArray
      }
      catch {
        return []
      }
    }

  },
  methods: {
    changeClass() {
      this.width = document.documentElement.clientWidth;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.blurb {

  margin: 20px;
  padding: 0;
  align-content: center;
  text-align: center;
}

.smallBlurb {
  width: 100%;
  flex-grow: 1
}

.largeBlurb {
  width: 60%;
  flex-grow: 1
}

.icon {
  width: 56px;
  height: 56px;
  margin-left: 7px;
  margin-right: 7px;
  padding-top: 2px;
  padding-bottom: 2px;
  margin-top: auto;
  margin-bottom: auto;
}

.iconMiddle {
  width: 60px;
  height: 60px;
  margin-left: auto;
  margin-right: auto;
  margin-top: auto;
  margin-bottom: auto;
}

.iconLegend {
  width: 40px;
  height: 40px;
  margin-left: 10px;
  margin-right: 10px;
  margin-top: auto;
  margin-bottom: auto;
}

.iconsTogether {
  width: 140px;
}

.subsection {
  text-align: left;
  display: flex;
}

h3 {
  margin: 8px 0px;
  margin-top: 12px;
  margin-bottom: 6px;
  padding: 0px;
  text-align: left;
}

p {
  margin-top: 0px;
  margin-bottom: 5px;
}

.subsectionLegend {
  text-align: left;
  /*display: flex;*/
  border: grey 1px solid;
  padding: 10px
}

.legendItem {
  display: flex
}

.subsectiondescription {
  display: flex;
  padding-left: 10px;
  align-items: center;
}


.parentContainer {
  display: flex;
  flex-flow: row wrap;
}

.legendLarge {
  width: 36%;

  padding: 2%;
  float: left;
  left: 20vw;
  /*padding: 10px
  /*flex-grow: 4*/
}

.legendSmall {
  padding: 2%;
  /*padding: 10px
  /*flex-grow: 4*/
  margin-left: auto;
  margin-right: auto
}</style>
