# helper function version 1.0
# created for notebook style control, video embeding, code hide/show, etc.
# Kaveh Jahanshahi - 26/May/2020

from IPython.display import Math, HTML, display, Latex, YouTubeVideo, clear_output
from os import path


def toggle_code(title="answer", on_load_hide=True, above=1):
    if above < 1:
        print("Error: please input a valid value for 'above'")
    else:
        display_string = """
    <script>
      function get_new_label(butn, hide) {
          var shown = $(butn).parents("div.cell.code_cell").find('div.input').is(':visible');
          var title = $(butn).val().substr($(butn).val().indexOf(" ") + 1)
          return ((shown) ? 'Show ' : 'Hide ') + title
      }
      function code_toggle(butn, hide) {
        $(butn).val(get_new_label(butn,hide));
        $(hide).slideToggle();
      };
    </script>
    <input type="submit" value='initiated' class='toggle_button'>
    <script>
        var hide_area = $(".toggle_button[value='initiated']").parents('div.cell').prevAll().addBack().slice(-""" + str(above) + """)
        hide_area = $(hide_area).find("div.input").add($(hide_area).filter("div.text_cell"))
        $(".toggle_button[value='initiated']").prop("hide_area", hide_area)
        $(".toggle_button[value='initiated']").click(function(){
            code_toggle(this, $(this).prop("hide_area"))
        });
$(".toggle_button[value='initiated']").parents("div.output_area").insertBefore($(".toggle_button[value='initiated']").parents("div.output").find('div.output_area').first());
    var shown = $(".toggle_button[value='initiated']").parents("div.cell.code_cell").find('div.input').is(':visible');
    var title = ((shown) ? 'Hide ' : 'Show ') + '""" + title + """';
    """
    if on_load_hide:
        display_string += """ $(".toggle_button[value='initiated']").addClass("init_show");
            $(hide_area).addClass("init_hidden"); """
    else:
        display_string += """ $(".toggle_button[value='initiated']").addClass("init_hide");
            $(hide_area).addClass("init_shown"); """

    display_string += """ $(".toggle_button[value='initiated']").val(title);
    </script>"""
    display(HTML(display_string))


def set_notebook_preferences(home_button = True):

    css_file = path.join(path.dirname(__file__), 'notebook.css')
    css = open(css_file, "r").read()

    display_string = "<style>" + css + "</style>"

    if (home_button):
        display_string += """
     <input type="submit" value='Home' id="initiated" class='home_button' onclick='window.location="../Index.ipynb"' style='float: right; margin-right: 40px;'>
    <script>
    $('.home_button').not('#initiated').remove();
    $('.home_button').removeAttr('id');
    $(".home_button").insertBefore($("div.cell").first());
    """

    else:
        display_string += "<script>$('.home_button').remove();"

    display_string += """
    $('div.input.init_hidden').hide()
    $('div.input.init_shown').show()
    $('.toggle_button').each(function( index, element ) {
       var prefix;
       if (this.classList.contains('init_show')) {
           prefix = 'Show '
       }
       else if (this.classList.contains('init_hide')) {
           prefix = 'Hide '
       };
       $(this).val(prefix + $(this).val().substr($(this).val().indexOf(" ") + 1))
    });
    IPython.OutputArea.prototype._should_scroll = function(lines) {
        return false;
    }
    </script>
    """
    display(HTML(display_string))
