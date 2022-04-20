---
layout: data_jp
title: "Wget Data"
description: "C-PROOF Glider Data"
header-img: "img/MikeSaanich19.jpg"
---

<script>
//https://stackoverflow.com/questions/45615998/on-click-copy-to-clipboard/45616055
function copyToClipboard(element) {
  var $temp = $("<input>");
  $("body").append($temp);
  $temp.val($(element).text()).select();
  document.execCommand("copy");
  $temp.remove();
}
</script>

<style>
/*https://stackoverflow.com/questions/7117073/add-a-tooltip-to-a-div*/
[data-tooltip]:before {
    content: attr(data-tooltip);
    position: absolute;
    opacity: 0;
    
    /* customizable */
    transition: 0.2s;
    padding: 10px;
    color: #FFFFFF;
    border-radius: 5px;
    box-shadow: 2px 2px 1px silver;  
    font-size: 12px;
    line-height: 16px;
}
[data-tooltip]:hover:before {
    opacity: 1;
    /* customizable */
    background: #979BA0;
    margin-top: -35px;
  /*  margin-left: 60px;*/
}

[data-tooltip]:not([data-tooltip-persistent]):before {
    pointer-events: none;
}

</style>

# Downloading Glider Data

## Get glider data:

The science files are created in `L0_timeseries` and `L0_gridfiles`. These are proper nectdf files that have metadata and attributes, and should be compliant with US-IOOS standards.

By default, the wget will download data to the directory the user is in. \
If you would like save the data in a different location use the flag  \
`--directory-prefix=outdir`  \
 where `outdir` is the name of the directory you would like to download data to. 

To download `all mission data`, type command

<div data-tooltip="Click to copy" class="language-plaintext highlighter-rouge "><div class="highlight"><pre class="highlight"><code id="copy4" onclick="copyToClipboard('#copy4')">wget -N --directory-prefix=outdir --input-file=http://cproof.uvic.ca/gliderdata/deployments/mission_all.txt
</code></pre></div></div>

To download all the data by glider line or by platform, replace `mission_all.txt` with one of the following:

### Glider lines

`LineP.txt`

`CalvertLine.txt`

### Platforms 

`dfo-bb046.txt`

`dfo-[[ glidername ]].txt`

