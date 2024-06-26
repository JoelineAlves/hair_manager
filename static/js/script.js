/* global $ */
$(document).ready(function() {
    $(".sidenav").sidenav({ edge: "right" });
    $("select").formSelect();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    
    // Custom validation taken from Code Institute Mini Project tutorial
    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function() {
            $(this).parent(".select-wrapper").on("change", function() {
                if ($(this).children("ul").children("li.selected:not(.disabled)").length > 0) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function() {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").length > 0) {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function() {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});