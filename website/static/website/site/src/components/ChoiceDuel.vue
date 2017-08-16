<template>
  <div>
    <form>
      <div class="form-group">
        <label class="form-label">Duelo de:</label>
        <label class="form-radio" v-for="i in issues">
          <input type="radio" v-model="issue" name="issue" :value="i" />
          <i class="form-icon"></i> {{i}}
        </label>
      </div>
      <button class="btn btn-primary" :class="{'loading': creating}" type="button" @click="createDuel">
        Crear duelo
      </button>
    </form>
  </div>
</template>

<script>
import Clipboard from 'clipboard'
var clipboard = new Clipboard('.btn')
console.log('clipboard:', clipboard)

export default {
  props: ['issues'],
  name: 'ChoiceDuel',
  data () {
    return {
      issue: 'python',
      link: 'https://adlasd.com/duelo/asdasdamsdklm2klm',
      creating: false
    }
  },
  methods: {
    createDuel () {
      this.creating = true
      this.$emit('createDuel', this.issue)
    }
  }
}

</script>
