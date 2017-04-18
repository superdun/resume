/**
 * Created by dun on 17-2-24.
 */



$(document).ready(function () {

    $('ul.tabs').tabs('select_tab', 'tab_id');
    $("#send").click(function () {
        var text = $('#text').val();
        if (!text) {
            alert("还木有输入词。。没墨不")
        }
        else {
            var formData = new FormData();
            formData.append("text", text);
            if ($("#swipe-e").attr("class").indexOf("active") > 0) {
                formData.append("mode", "e");
            }
            else {
                formData.append("mode", "j");
            }
            $.ajax({
                url: 'api/translation',
                type: 'POST',
                data: formData,
                contentType: false,
                processData: false,
                success: function (result) {
                    if (result["status"] == "ok") {
                        for (var i in result["msg"]) {
                            if (result["msg"][i]["content"]){
                                $("#"+i).text(result["msg"][i]["content"]);
                            }
                            else {
                                $("#"+i).text("木有找到。。")
                            }


                            $("#"+i+"_url").attr("href",result["msg"][i]["url"]);
                        }
                    }
                    else{
                        alert("还没做好哦  T_T")
                    }
                }
            })
        }
    })
});







