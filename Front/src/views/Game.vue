<template>
  <div class="game-container">
    <div class="top-menu">
      <div class="actual-day" style="font-size: 28pt;">
        День - {{ day }}
      </div>
    </div>

    <div class="outer" style="height:80vh; width: 90%; margin-left: 5%" v-if="descr != ''">
      <div class="inner">


        <div class="card-box">
          <div
              style="font-size: 20pt; word-wrap: break-word; padding-left: 10px; padding-right: 10px; padding-top: 50px;">
            <b>{{ descr }}</b><br />

            <img :src="pic" style="margin-top: 50px; height: 550px; margin-bottom: 50px;"/>
          </div>
        </div>
        <div style="
            width: 70%;
            margin-left: 15%;
            background: rgba(255,255,255,0.8);
            padding-bottom: 15px;
            ">
          <a-button v-for="(item, index) in this.answers"
                    style="white-space: normal; display: inline-flex; justify-content: center; width: 48%; font-size: 20pt; height: 100px;" :disabled="dis"
                    @click="sendAnswer(item.id_event)">
            {{ item.description }}
          </a-button>
        </div>
      </div>
    </div>

    <div class="bottom-menu">
      <a-row class="profile-game">
        <a-col :span="5">
          <a-avatar :size="128" :src="this.profileUser.pic" style="margin: 15px;"/>
        </a-col>
        <a-col :span="15" class="stats-game" style="font-size: 14pt; padding-bottom: 15px;">
          <div>
            <div style="display: inline-block">
              <a-icon type="heart" theme="twoTone" twoToneColor="#eb2f96"/>
            </div>
            <a-progress :percent="user.health" :strokeColor="{  '0%': '#eb2f96', '100%': '#eb2f96'}"/>
          </div>

          <div>
            <div style="display: inline-block">
              <a-icon type="dollar" style="color:rgb(235, 134, 47);"/>
            </div>
            <a-progress :percent="user.money" :strokeColor="{  '0%': 'rgb(235, 134, 47)', '100%': 'rgb(235, 134, 47)'}"/>
          </div>

          <div>
            <div style="display: inline-block">
              <a-icon type="smile" theme="twoTone" twoToneColor="rgb(62, 181, 98)"/>
            </div>
            <a-progress :percent="user.point" :strokeColor="{  '0%': 'rgb(62, 181, 98)', '100%': 'rgb(62, 181, 98)'}"/>
          </div>
        </a-col>
      </a-row>
    </div>
  </div>
</template>

<script>
import {newGame, reloadGame, sendAnswer, resumeGame} from '@/api/game'
import {getProfile} from "../api/auth";

export default {
  data() {
    return {
      dis: false,
      user: {
        name: '',
        health: 0,
        money: 0,
        point: 0,
        round: 0
      },

      pic: '',
      day: 0,
      left: '',
      right: '',
      descr: '',

      leftAction: {}

    }
  },
  methods: {
    async startNewGame() {
      let id = this.$route.query.id
      if (!id) {
        this.$router.push({path: 'start'})
        return
      }
      this.$router.replace({id: '-1'})


      let res = await newGame(localStorage.getItem('session'), id)
      this.day = res.round
      this.descr = res.description
      this.left = res.left_answer
      this.right = res.right_answer

      this.pic = res.pic
      this.user.name = res.name
      this.user.health = res.health
      this.user.money = res.money
      this.user.point = res.point
      this.user.round = res.round

      let profile = getProfile()
      if (profile !== false) {
        this.profileUser = profile;
        profile.then(val => {
          this.profileUser = val
          console.log("Профиль: ", this.profileUser)
          this.user.pic = this.profileUser.pic;
          this.user.name = this.profileUser.names;
        });
      }

    },

    async resumeGame() {
      let res = await resumeGame(localStorage.getItem('session'))
      this.day = res.round
      this.descr = res.description
      this.left = res.left_answer
      this.right = res.right_answer
      this.answers = res.answer;
      console.log(this.answers);

      this.pic = res.pic
      this.user.health = res.health
      this.user.money = res.money
      this.user.point = res.point
      this.user.round = res.round
    },

    async sendAnswer(ans) {
      this.dis = true
      let res = await sendAnswer(localStorage.getItem('session'), ans)
      if (res.end === true) {
        this.$warning({
          title: `Вы проиграли. Прожито дней ${this.day}`
        })
        this.$router.push({path: 'start'})
      }
      console.log(res);
      console.log(res.health)
      console.log(this.user.health)
      console.log(res.health - this.user.health)

      let Shealth = res.health - this.user.health
      let Seat = res.food - this.user.eat
      let Scomm = res.communication - this.user.comm
      let Shome = res.leisure - this.user.home

      this.day = res.round
      this.descr = res.description
      this.left = res.left_answer
      this.right = res.right_answer


      let profile = getProfile()
      if (profile !== false) {
        this.profileUser = profile;
        profile.then(val => {
          this.profileUser = val
          console.log("Профиль: ", this.profileUser.pic);
          this.user.pic = this.profileUser.pic;
          this.user.name = this.profileUser.names;
          this.user.health = this.profileUser.health;
          this.user.money = this.profileUser.money;
          this.user.point = this.profileUser.point;
          this.user.round = this.profileUser.round;
        });
      }

      this.dis = false
    }

  },
  mounted() {

    let profile = getProfile()
    if (profile !== false) {
      this.profileUser = profile;
      profile.then(val => {
        this.profileUser = val
        console.log("Профиль: ", this.profileUser.pic);
        this.user.pic = this.profileUser.pic;
        this.user.name = this.profileUser.names;
      });
    }

    let type = this.$route.query.type
    if (type === 'resume') {
      this.resumeGame()
      return
    }
    this.startNewGame();
  },

};
</script>
<style>
.right {
  margin-left: 15px;
}

.left {
  margin-right: 15px;
}

.left > .ant-btn-icon-only {
  width: 64px;
  height: 64px;
}

.right > .ant-btn-icon-only {
  width: 64px;
  height: 64px;
}

.outer:before {
  content: '';
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}

.inner {
  width: 100%;
  display: inline-block;
  vertical-align: middle;
}

.outer {
  text-align: center;
}

.left, .right, .card-box {
  display: inline-block;
}

.center-menu {
  margin-top: 80px;
  width: 30%;
  margin-left: 35%;
}

.card-box {
  width: 70%;
  background: rgba(255, 255, 255, 0.8);
}

.actual-day {
  font-size: 24px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 0px 0px 5px 5px;
  width: 50%;
  top: 0px;
  margin-left: 25%;
}

.game-container {
  height: 100vh;
  width: 100vw;
}

.center-menu {
  vertical-align: middle;
}

.stats-game {
  margin-left: 30px;
  margin-top: 10px;
  text-align: left
}

.ant-progress-line {
  margin-left: 10px;
  width: 80% !important;
}

.bottom-menu {
  border: solid 1.2px black;
  border-radius: 5px 5px 0px 0px;
  left: 25%;
  width: 50%;
  min-width: 550px;
  background: rgba(255, 255, 255, 0.8);
  position: absolute;
  bottom: 0px;
}

</style>
