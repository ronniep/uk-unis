<template>
  <UniData :UniShort="this.shortUni" :UniName="this.nameUni"/>
</template>

<script>
import './assets/css/main.css';
import UniData from "./components/UniData.vue"


export default {
  name: 'AppUni',
  components: {
    UniData
  },
  data() {
    return {
            shortUni: 'TUD',
            nameUni: 'TU Delft',
        }
  }

};

</script>

<style></style>
