<template>
<div>
<!-- title -->
<div id="title" class="animated">Vusion</div>
<!-- Main -->
  <v-layout row wrap>
    <v-flex md3>
    <!-- empty -->
    </v-flex>
    <v-flex md6 xs12>
      <!-- buttons -->
      <div class="optionButtons">
            <input style="display: none;" type="file" @change="onFileSelected" ref="pictureInput" accept="image/jpeg, image/png">
            <button @click="$refs.pictureInput.click()" class="uploadPhoto" id="myPicture">Choose a picture</button>
            <br>
            <br>
            <v-btn @click="onUpload" title="Fire!" fab color="white" depressed small><div style="color: #4DB6AC;"><v-icon dark>send</v-icon></div></v-btn>
      </div>
      <!-- output -->
      <div class="outBox">
        <v-layout row>
          <v-flex xs1>
            <!-- empty -->
          </v-flex>
          <v-flex xs10 md12 class="output">
            {{pleaseWait}}
            {{indicator}}
            <div style="color: red;">{{error}}</div>
            <div
            v-for="element in output"
            v-bind:item="element"
            v-bind:key="element._id"
            >
            <div
            v-for="key in element"
            v-bind:item="key"
            v-bind:key="key._id"
            >
            <v-layout row style="padding: 10px;">
              <v-flex xs6 style="text-align: left;"><strong style="color: gray;">Detected:</strong> {{Object.keys(element)[0]}}</v-flex>
              <v-flex xs6 style="text-align: right;"><strong style="color: gray;">Probability:</strong> {{key}}</v-flex>
            </v-layout>
            </div>
            </div>
          </v-flex>
          <v-flex xs1>
            <!-- empty -->
          </v-flex>
        </v-layout>
      </div>
    </v-flex>
    <v-flex md3>
<!-- empty -->
    </v-flex>
  </v-layout>
  <!-- alert -->
  <br>
  <div id="popup">
    <v-layout row>
    <v-flex md3>
      <!-- empty -->
    </v-flex>
    <v-flex md6 xs12>
      <v-alert
      v-model="alert"
      icon="thumb_up"
      transition="scale-transition"
      dismissible
      color="#00897B"
    >
      If you really like this webapp, you can donate or contribute to it on <a href="http://www.github.com/Merwanedr/vusion"><strong>Github</strong>.</a>
    </v-alert>
    </v-flex>
    <v-flex md3>
      <!-- empty -->
    </v-flex>
  </v-layout>
  </div>
  <v-footer class="pa-3" fixed color="#00897B" style="text-align: center;">
      <v-layout row>
        <v-flex xs2></v-flex>
         <v-flex xs8><strong><a href="http://www.github.com/Merwanedr/vusion" target="_blank"><div style="color: white;">&copy; {{ new Date().getFullYear() }} Merwane Draï</div></a></strong></v-flex>
         <!-- Just kidding, no copyrights here -->
         <v-flex xs2></v-flex>
      </v-layout>
  </v-footer>
</div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Home',
  data() {
    return {
      selectedFile: null,
      pleaseWait: '',
      indicator: '',
      error: '',
      output: null,
      alert: true
    }
  },
  created() {
    this.indicator = 'Output will be displayed here.';
  },
    methods: {
    onFileSelected(event){
      this.selectedFile = event.target.files[0]
    },
    onUpload() {
      this.output = null
      if (this.selectedFile == null) {
        this.indicator = '';
        this.error = 'Please select a file before';
      }
      else {
      this.indicator = '';
      this.error = '';
      this.pleaseWait = 'Please wait ...';
      const fd = new FormData();
      fd.append('file', this.selectedFile, this.selectedFile.name);
      this.pleaseWait = 'Please wait...';
        axios.post('http://127.0.0.1:5000/', fd)
      .then(res => {
        this.pleaseWait = '';
        this.error = '';
        console.log(res);
        this.output = res.data
        this.selectedFile = null;
      })
      this.selectedFile = null;
      }
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a{
  text-decoration: none;
  color: white;
}
a:visited{
  text-decoration: none;
  color: white;
}
#title{
  text-align: center;
  font-family: 'Ubuntu', sans-serif;
  margin-top: 40px;
  font-size: 50px;
}
.animated {
  margin: 0;
  padding: 0;
  background: url('../assets/rainbow.gif') no-repeat;
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
}
.optionButtons{
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-top: 50px;
}
.subjectSelect{
  background-color: white;
  border: none;
  border-radius: 50px;
  margin-top: 15px;
  width: 200px;
  height: 30px;
  padding-left: 50px;
  resize: none;
  padding-top: 1px;
  color: #4DB6AC;
  text-align: center;
}
.subjectSelect:focus{
  outline: none;
}
.uploadPhoto{
  background-color: white;
  border: none;
  border-radius: 50px;
  margin-top: 15px;
  width: 200px;
  height: 30px;
  padding-left: 5px;
  resize: none;
  padding-top: 1px;
  color: #4DB6AC;
  text-align: center;
}
.uploadPhoto:focus{
  outline: none;
}
.outBox{
  margin-top: 40px;

}
.output{
  background-color: white;
  border-radius: 10px;
  padding: 10px;
  text-align: center;
}
#popup{
  animation: cssAnimation 0s 60s forwards;
  visibility: hidden;
}
@keyframes cssAnimation {
  to   { visibility: visible; }
}
</style>
