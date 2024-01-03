<template>
    <header @click="toggle" class="faqtitle">
      <h2><img class="arrow" width="16" :src="require('../assets/'+image+'.png')"> <slot name="header"></slot></h2>
    </header>
    <main :style="displayStyle" class="faqmain">
      <slot name="default"></slot>
    </main>
</template>

<script>
export default {
  name: 'FaqExpandable',
  data() {
    return {
      open: false,
      image: "arrowright"
    }
  },
  methods: {
    toggle() {
      this.open = !(this.open)
      if (this.open) {
        this.image = "arrowdown"
      } else {
        this.image = "arrowright"
      }
    }
  },
  computed: {
    displayStyle() {
      return this.open ? "display: block" : "display: none"
    }
  }
}
</script>


<style>



h2{
  margin: 10px 0px;
  font-size: larger;
  text-align: left;
}

.arrow{
  margin-right: 8px;
}

</style>