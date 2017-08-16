import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import DuelRomm from '@/components/DuelRomm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/duelo/:duel',
      name: 'DuelRomm',
      component: DuelRomm
    }
  ],
  mode: 'history'
})
