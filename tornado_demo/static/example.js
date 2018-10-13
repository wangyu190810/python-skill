var app = new Vue({
  el: '#app',
  data: {
    message: {
        "user":"asdfasdf"
    }
  },
  methods:{
    fetchDate:function(){
      var xhr = new XMLHttpRequest()
      var self = this
      xhr.open("GET","http://127.0.0.1:9999/app")
      xhr.onload = function(){
        self.message = JSON.parse(xhr.responseText)
      }
      xhr.send()
    }
  }
})
