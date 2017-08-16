<template>
  <div class="container">
    <div class="columns">
      <div class="column col-3"></div>
      <div class="column col-6">
        <choice-duel :issues="issues" @createDuel="createDuel"></choice-duel>        
        <div class="input-group" v-if="showLink">
          <span class="input-group-addon" :value="link" id="link">{{link}}</span>
          <button type="button" class="btn btn-primary input-group-btn" data-clipboard-target="#link">copiar</button>
        </div>

      </div>
      <div class="column col-3"></div>
    </div>
  </div>
</template>

<script>
import ChoiceDuel from '@/components/ChoiceDuel'

export default {
  name: 'hello',
  data () {
    return {
      issues: ['python'],
      link: 'https://adlasd.com/duelo/asdasdamsdklm2klm',
      showLink: false
    }
  },
  methods: {
    createDuel (issue) {
      let duel = 'Dgd3'
      setTimeout(() => {
        this.$router.push(`/duelo/${duel}`)
      }, 1000)
    }
  },
  components: {
    'choice-duel': ChoiceDuel
  }
}
</script>

<style>
</style>
