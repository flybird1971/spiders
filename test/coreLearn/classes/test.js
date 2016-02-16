var TM = {
    arr : [],
    getNodes : function(tagNames, models) { 
        var m = models ? models : this.model;
        var c = null;
        var arr = this.arr;  
        // 数组传递也是<a href="https://www.baidu.com/s?wd=%E5%BC%95%E7%94%A8%E4%BC%A0%E9%80%92&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dWPhRzP1PBnhnsPWKbnHuB0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6KdThsqpZwYTjCEQLGCpyw9Uz4Bmy-bIi4WUvYETgN-TLwGUv3ErjT1PHfknj0krjRkPj6znjbz" target="_blank" class="baidu-highlight">引用传递</a>
        if(c = m.children){ 
            for(var i = 0; i < c.length; i++) { 
                var nc = c[i].tagName.toLowerCase(); 
                if(nc == tagNames){  
                    arr.push(c[i]); // 引用被改变，原来的也改变
                }else{
                    this.getNodes(tagNames, c[i]);
                }
            }
        } 
        return arr;
    }
};

function test(){

    // $('#test-id').attr('src','https://github.com/arrix/node-readability'+ "&output=embed")

    // $.ajax({
        // url: 'https://github.com/arrix/node-readability',
        // // type: 'GET',
        // // dataType: 'html',
        // type: "POST",
        // contentType: "application/json",
        // dataType:'jsonp',
        // // data: {param1: 'value1'},
        // complete: function(xhr, textStatus) {
        //     // console.log(xhr);
        //     //called when complete
            
        // },
        // success: function(data, textStatus, xhr) {
        //     console.log(data);
        //     console.log(textStatus);
        //     console.log(xhr);
        //     //called when successful
        // },
        // error: function(xhr, textStatus, errorThrown) {
        //     //called when there is an error
        // }
    // });
}



curl(
    // fetch all of these resources ("dependencies")
    [
        'stuff/three', // an AMD module
        // 'cssx/css!stuff/base', // a css file
        // 'i18n!stuff/nls/strings', // a translation file
        // 'text!stuff/template.html', // an html template
        'stuff/template.html', // an html template
        'domReady!'
    ]
)
// when they are loaded
.then(
    // execute this callback, passing all dependencies as params
    function (three, link, strings, template) {
        var body = document.body;
        if (body) {
            body.appendChild(document.createTextNode('three == ' + three.toString() + ' '));
            body.appendChild(document.createElement('br'));
            body.appendChild(document.createTextNode(strings.hello));
            body.appendChild(document.createElement('div')).innerHTML = template;
        }
    },
    // execute this callback if there was a problem
    function (ex) {
        var msg = 'OH SNAP: ' + ex.message;
        alert(msg);
    }
);


// test()
// TM.getNodes('body',document.all[0])[0];
// var res = TM.getNodes('body',document.all[0]);
// console.log(res)