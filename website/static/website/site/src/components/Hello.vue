<template>
  <div class="container">
    <div class="columns">
      <div class="column col-3"></div>
      <div class="column col-6">
        <form>
          <div class="form-group">
            <label class="form-label">Duelo de:</label>
            <label class="form-radio">
              <input type="radio" v-model="issue" name="issue" value="python" />
              <i class="form-icon"></i> Python
            </label>
            <label class="form-radio">
              <input type="radio" v-model="issue" name="issue" value="other"/>
              <i class="form-icon"></i> Otro
            </label>
          </div>
          <button v-show="!showLink" class="btn btn-primary" type="button" @click="generateLink()">Generar enlace para compartir</button>
          <div class="input-group" v-if="showLink">
            <span class="input-group-addon" :value="link" id="link">{{link}}</span>
            <button type="button" class="btn btn-primary input-group-btn" data-clipboard-target="#link">copiar</button>
          </div>
        </form>
      </div>
      <div class="column col-3"></div>
    </div>
  </div>
</template>

<script>
import Clipboard from 'clipboard'
var clipboard = new Clipboard('.btn')
console.log('clipboard:', clipboard)
export default {
  name: 'hello',
  data () {
    return {
      issue: 'python',
      link: 'https://adlasd.com/duelo/asdasdamsdklm2klm',
      showLink: false
    }
  },
  methods: {
    generateLink () {
      this.showLink = true
    }
  }
}
</script>

<style>
@import '../../node_modules/spectre.css/dist/spectre.min.css';
@import '../../node_modules/spectre.css/dist/spectre-icons.min.css';
</style>
