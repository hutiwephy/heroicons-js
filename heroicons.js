(function (){
    var db = $ICONDB;

    document.head.innerHTML += '<style>$ICONCSS</style>';

    const observer = new MutationObserver(()=>{
        var icons = document.querySelectorAll('i[class*="hicon-"]');
        for (var i=0; i < icons.length; i++){
            var icon = icons[i];
            for (var j=0; j < icon.classList.length; j++){
                if (icon.classList[j].startsWith("hicon-")){
                    var name = icon.classList[j];
                    var args = name.split("-");
                    if (args.length < 3){ continue; }

                    var svgcode = db[args[1]][name.substring(args[0].length + 1 + args[1].length + 1)];
                    if (svgcode == undefined){ continue; }

                    var div = document.createElement("div");
                    div.innerHTML = svgcode;

                    for(var k=0; k<icon.classList.length; k++){
                        div.firstChild.classList.add(icon.classList[k]);
                    }
                    if(icon.id != ""){
                        div.firstChild.id = icon.id;
                    }

                    icon.replaceWith(div.firstChild);
                    delete div;
                }
            }
        }
    });

    observer.observe(document.body, {
        attributes: true,
        childList: true,
        subtree: true,
    });
})();