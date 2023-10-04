'use strict';
$(() => {
  $('INPUT#btn_translate').click(() => {
    const translateUrl = 'https://fourtonfish.com';
    const code = $('INPUT#language_code').val();

    // For language codes
    // see https://www.loc.gov/standards/iso639-2/php/code_list.php
    $.get(`${translateUrl}/hellosalut/?lang=${code}`, (data, status) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
