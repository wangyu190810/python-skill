// var Vue = request("vue");
// Vue.use(request("vue-resource"));
// Vue.http.headers.common["Authorization"] = "no key"

new Vue({
  el: '#user',
  data: {
    message: 'Hello'
  },
  methods:{
    fetchDate:function(){
      var xhr = new XMLHttpRequest()
      var self = this
      xhr.open("GET","/userinfo")
      xhr.onload = function(){
        self.message = JSON.parse(xhr.responseText)
      }
      xhr.send()
    },

    userinfo:function (event) {
        e.preventDefault();
        var req= this.$http.get(
          "/userinfo",
          function(data,status,request){
            this.message = data;
          }

        )

    }
  }
})
