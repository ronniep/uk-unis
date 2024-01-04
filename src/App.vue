<template>
  <div class="house">
    <div class="midcontainer">
      <MenuBar />
      <div class="titlediv">
    <h1>How is UK academia tied to the fossil fuel industry?</h1>
  </div>

  <h3><b>Please note! This database is a work in progress and not yet publicly launched! There may be inaccuracies in the data.</b>
  </h3>

      <div class="blurbbegin">
        <h2>Database of ties between UK academia and the fossil fuel industry</h2>
<p>
          This web portal shows the ongoing decentralised research by a coalition of organisations into the
          relationships between UK universities and research funding bodies, and the fossil fuel industry. The database
          shows different types of
          fossil ties per institution since the Paris Agreement (2015), such as (co-)funding of research and professors,
          sponsoring of students' studies and activities, presentations of the fossil fuel industry at career events or as
          part of the study programme, and more. The database is regularly updated while new information comes in, and we
          check all information before publishing here: only confirmed ties for which we have evidence are displayed.
        </p>
        <p>The database functions as an information source for investigative journalists, action groups, students,
          university staff and administrators, NGOs, policymakers, and the public.
        </p>
        <div class="moveToMiddle"><button class="blurbbegin" @click="goToFullDatabase()" type="button">See full
            database</button>
        </div>
      </div>
      <div class="blurbBeginNoColour">
        <h2>Why map the ties between academia and the fossil fuel industry?</h2>
        <p>There has been increasing social scrutiny of the close ties between universities and the fossil fuel industry.
          For an informed discussion about whether fossil fuel companies, lobby organisations or research institutes
          should be present on campus and in what capacity, we are documenting all current relationships between UK
          universities and research funding bodies, and these companies.
        </p>
        <!--
        <p>Funding from fossil companies has been shown to bias research in favour of fossil fuels, and may
          influence the direction of research towards technologies which will least disrupt fossil companies' business
          model, rather than those most necessary for an energy transition.
        </p>
        <p>The presence of such companies on campus - at careers fairs, guest lectures and sponsoring students
          organisations,
          for example - can be seen as a tacit endorsement by the university of them and their activities, and
          contributes to their 'social licence to operate', i.e. their perceived legitimacy in the eyes of the public.
        </p>
        <p>Increasingly, academics and students are demanding that their research institutions stop association with
          fossil companies. This would target a key blocker of the energy transition, namely the influence of fossil
          fuel companies on the direction of research & development, public opinion and policymakers.</p>
        -->
        <div class="moveToMiddle">
            <button class="backButton" onclick="window.location.assign('./FAQ.html')"
            type="button">Go to FAQs to read more</button>
            <button class="backButton" onclick="window.location.assign('./News.html')"
            type="button">Fossil Ties in the News</button>
        </div>
      </div>
      <div class="blurbbegin">
        <h2>About the coalition</h2>
        <p>This project involves collaboration by a <b>coalition of local and national
            organisations</b>. We support and coordinate
          decentralised research into relationships between academia and the fossil fuel industry. We do this through
          decentralised information gathering on campuses, freedom of information (FOI) requests, and crowdsourcing.</p>
          <!--

          <div id="logos" class="moveToMiddle">
          <a href="https://endfossil.com/" target="_blank"><img class="thumb"
              :src="require('./assets/logo_thumbs/logo_EFO.png')" width="80"></a>
          <a href="https://gofossilfree.org/nl/" target="_blank"><img class="thumb"
              :src="require('./assets/logo_thumbs/logo_fv.png')" width="80"></a>
          <a href="https://milieudefensie.nl/over-ons/milieudefensie-jong" target="_blank"><img class="thumb"
              :src="require('./assets/logo_thumbs/logo_MDJ.png')" width="80"></a>
          <a href="https://verbiedfossielereclame.nl/" target="_blank"><img class="thumb"
              :src="require('./assets/logo_thumbs/logo_rf.jpg')" width="80"></a>
          <a href="https://scientists4future.nl/" target="_blank"><img class="thumb"
              :src="require('./assets/logo_thumbs/logo_s4f.png')" width="80"></a>
          <a href="https://www.scientistrebellion.nl/" target="_blank"><img class="thumb"
              :src="require('./assets/logo_thumbs/logo_sr.png')" width="80"></a>
          <a href="https://www.solid-sustainability.org/" target="_blank"><img class="thumb"
              :src="require('./assets/logo_thumbs/logo_ssr2.jpg')" width="80"></a>
          <a href="https://socialtippingpointcoalitie.nl/" target="_blank"><img class="thumb"
              :src="require('./assets/logo_thumbs/logo_STPC.png')" width="80"></a>
          <a href="http://universityrebellion.nl/" target="_blank"><img class="thumb"
              :src="require('./assets/logo_thumbs/logo_UR.png')" width="80"></a>
        </div>
-->
        <div class="moveToMiddle"><button class="blurbbegin" onclick="window.location.assign('./About.html')"
            type="button">Read more</button>
        </div>
      </div>
      <div class="blurbEndNoColour">
          <h2 class="moveToMiddle">How can I help?</h2>

        <!--<p>There are many ways to contribute to this research project:</p>-->
        <div class="containInfoBoxes">
          <div class="infoBox">
            <p>Want to research fossil ties at your place of work or study?</p>
            <button class="blurbbegin" onclick="window.open('https://www.solid-sustainability.org/handbook')"
            type="button">Check out our handbook!</button>
          </div>
          <div class="infoBox">
            <p>
            Do you know of a fossil tie that's not on this website? 
            </p>
              <button class="blurbbegin" onclick="window.open('https://www.educationclimatecoalition.co.uk/contact-us')"
            type="button">Tell us about it!</button>
          </div>
          <div class="infoBox"><p>Are you from outside the UK, and want to investigate fossil ties in your country?</p>
            <button class="blurbbegin" onclick="window.open('mailto:info@solid-sustainability.org')"
            type="button">Get in touch!</button>
            </div>
        </div>
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
import MenuBar from './components/MenuBar.vue'
import './assets/css/main.css';

export default {
  name: 'App',
  components: {
    MenuBar
  },
  data() {
    return {
      uniNonSelected: true,
      shortUni: String,
      nameUni: String,
      width: document.documentElement.clientWidth
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
    },
    goToFullDatabase() {
      localStorage.removeItem("shortUni")
      localStorage.removeItem("nameUni")
      window.location.assign('./Database.html')
    },
    changeClass() {
      this.width = document.documentElement.clientWidth;
    }
  },
  mounted() {
    localStorage.removeItem("shortUni")
    localStorage.removeItem("nameUni")
    window.addEventListener('resize', this.changeClass);
  }
}
</script>


<style></style>