/*jslint browser: true*/
/*global $, jQuery, alert*/
var FLAG = 0;
$(document).ready(function () {
    "use strict";
    function fillProgress(i) {
        setTimeout(function () {
            if (FLAG === 0) {
                $("#progressbar li").eq(4 - i).addClass("active");
                i -= 1;
                if (i) {
                    fillProgress(i);
                }
            }
        }, 1000 * i);
    }
    function clearProgress() {
        var i;
        $("#progressbar li").eq(1).removeClass("error");
        for (i = 0; i < 5; i += 1) {
            $("#progressbar li").eq(i).removeClass("active");
        }
    }
    function completeProgress() {
        var i;
        for (i = 0; i < 5; i += 1) {
            $("#progressbar li").eq(i).addClass("active");
        }
    }

    $("#android_bot").hide();
    $("#submit").click(function () {
        var file_data,
            form_data,
            api_string,
            permission_string,
            actions_string,
            i;
        FLAG = 0;
        clearProgress();
        $("#mdl_body").html("");
        $("#android_bot").hide();
        if ($("#file_to_upload").val() !== "") {
            file_data = $("#file_to_upload").prop("files")[0];
            form_data = new FormData();
            form_data.append("file", file_data);
            $("#progressbar li").eq(0).addClass("active");
            $.ajax({
                url: "http://localhost:8000/upload",
                dataType: "text",
                cache: false,
                contentType: false,
                processData: false,
                data: form_data,
                type: "post",
                success: function () {
                    fillProgress(3);
                    $(".load").show();
                    $.ajax({
                        url: "http://localhost:8000/analyze",
                        dataType: "text",
                        cache: false,
                        contentType: false,
                        processData: false,
                        type: "post",
                        success: function (data) {
                            data = JSON.parse(data);
                            $(".load").hide();
                            if (data.result === "extractionfailed") {
                                $("#main_group").attr("fill", "lightgrey");
                                $("#result_text").text("Error! Please try again.");
                                $("#android_bot").show();
                                FLAG = 1;
                                clearProgress();
                                $("#progressbar li").eq(0).addClass("active");
                                $("#progressbar li").eq(1).addClass("error");
                            }
                            if (data.result === "benign") {
                                $("#main_group").attr("fill", "#a4c639");
                                $("#result_text").text("App is BENIGN");
                                $("#android_bot").show();
                                completeProgress();
                            }
                            if (data.result === "malware") {
                                $("#main_group").attr("fill", "#d91e18");
                                $("#result_text").text("App is MALICIOUS");
                                $("#android_bot").show();
                                completeProgress();
                            }
                            actions_string = "<p>Actions</p><pre><code>";
                            permission_string = "<p>Sensitive Permissions</p><pre><code>";
                            api_string = "<p>Sensitive API Calls</p><pre><code>";
                            for (i = 0; i < data.permissions.length; i += 1) {
                                permission_string += "<br>" + data.permissions[i];
                            }
                            permission_string += "<br></code></pre>";
                            for (i = 0; i < data.api.length; i += 1) {
                                api_string += "<br>" + data.api[i];
                            }
                            api_string += "<br></code></pre>";
                            $("#mdl_body").append(permission_string);
                            $("#mdl_body").append(api_string);
                            if (data.actions) {
                                $("#mdl_body").append(actions_string + JSON.stringify(data.actions, null, 2) + "</code></pre>");
                            }
                        }
                    });
                }
            });
        } else {
            alert("Please Upload File");
        }
    });
});
