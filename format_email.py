def format_email_html(booking_app_url,booking_app_remove_reservation_url,reservation_name,reservation_date,reservation_time,head_count,phone_number):
    return f"""
 <!--
* This email was built using Tabular.
* For more information, visit https://tabular.email
-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">
<head>
<title></title>
<meta charset="UTF-8" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<!--[if !mso]><!-->
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<!--<![endif]-->
<meta name="x-apple-disable-message-reformatting" content="" />
<meta content="target-densitydpi=device-dpi" name="viewport" />
<meta content="true" name="HandheldFriendly" />
<meta content="width=device-width" name="viewport" />
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no" />
<style type="text/css">
table {{
border-collapse: separate;
table-layout: fixed;
mso-table-lspace: 0pt;
mso-table-rspace: 0pt
}}
table td {{
border-collapse: collapse
}}
.ExternalClass {{
width: 100%
}}
.ExternalClass,
.ExternalClass p,
.ExternalClass span,
.ExternalClass font,
.ExternalClass td,
.ExternalClass div {{
line-height: 100%
}}
body, a, li, p, h1, h2, h3 {{
-ms-text-size-adjust: 100%;
-webkit-text-size-adjust: 100%;
}}
html {{
-webkit-text-size-adjust: none !important
}}
body, #innerTable {{
-webkit-font-smoothing: antialiased;
-moz-osx-font-smoothing: grayscale
}}
#innerTable img+div {{
display: none;
display: none !important
}}
img {{
Margin: 0;
padding: 0;
-ms-interpolation-mode: bicubic
}}
h1, h2, h3, p, a {{
line-height: 1;
overflow-wrap: normal;
white-space: normal;
word-break: break-word
}}
a {{
text-decoration: none
}}
h1, h2, h3, p {{
min-width: 100%!important;
width: 100%!important;
max-width: 100%!important;
display: inline-block!important;
border: 0;
padding: 0;
margin: 0
}}
a[x-apple-data-detectors] {{
color: inherit !important;
text-decoration: none !important;
font-size: inherit !important;
font-family: inherit !important;
font-weight: inherit !important;
line-height: inherit !important
}}
a[href^="mailto"],
a[href^="tel"],
a[href^="sms"] {{
color: inherit;
text-decoration: none
}}
</style>
<style type="text/css">
@media (min-width: 481px) {{
.hd {{ display: none!important }}
}}
</style>
<style type="text/css">
@media (max-width: 480px) {{
.hm {{ display: none!important }}
}}
</style>
<style type="text/css">
@media (min-width: 481px) {{
.t3{{mso-line-height-alt:45px!important;line-height:45px!important;display:block!important}}.t9{{padding-left:50px!important;padding-bottom:37px!important;padding-right:50px!important}}.t11{{padding-left:50px!important;padding-bottom:37px!important;padding-right:50px!important;width:500px!important}}.t15{{padding-bottom:15px!important;width:600px!important}}.t20{{padding-bottom:15px!important}}.t21{{line-height:26px!important;letter-spacing:-1.56px!important}}.t28{{padding:48px 50px 39px!important}}.t30{{padding:48px 50px 39px!important;width:500px!important}}.t34{{width:600px!important}}.t44{{padding-bottom:44px!important;width:800px!important}}.t49{{padding-bottom:44px!important}}.t74{{width:600px!important}}.t84{{width:800px!important}}.t94,.t99{{padding-bottom:1px!important}}.t113,.t123,.t134{{width:600px!important}}.t141{{mso-line-height-alt:0px!important;line-height:0!important;display:none!important}}.t144{{width:600px!important}}.t151{{mso-line-height-alt:0px!important;line-height:0!important;display:none!important}}.t152{{mso-line-height-alt:18px!important;line-height:18px!important}}.t154,.t162{{width:488px!important}}.t169{{background-color:#f8f8f8!important;padding:20px!important}}.t171{{background-color:#f8f8f8!important;padding:20px!important;width:560px!important}}.t175{{padding:20px 15px!important;width:570px!important}}.t180{{padding:20px 15px!important}}.t187{{max-width:310px!important}}.t188{{padding-left:5px!important;padding-right:5px!important}}.t195{{max-width:310px!important}}.t196{{padding-left:5px!important;padding-right:5px!important}}.t204{{max-width:600px!important}}.t213{{width:600px!important}}.t226{{padding-top:20px!important}}.t228{{padding-top:20px!important;width:560px!important}}.t232{{width:600px!important}}.t242{{max-width:800px!important}}.t251{{padding-left:10px!important;width:590px!important}}.t256{{padding-left:10px!important}}.t257{{font-size:14px!important}}.t259{{mso-line-height-alt:11px!important;line-height:11px!important}}.t261{{padding-left:10px!important;padding-bottom:16px!important;width:171px!important}}.t266{{padding-left:10px!important;padding-bottom:16px!important}}.t268{{mso-line-height-alt:9px!important;line-height:9px!important}}.t271{{padding-left:10px!important;width:590px!important}}.t276{{padding-left:10px!important}}.t277{{font-size:14px!important}}.t281{{padding-left:10px!important;padding-bottom:0!important;width:590px!important}}.t286{{padding-left:10px!important;padding-bottom:0!important}}.t291{{max-width:800px!important}}.t300{{padding-left:10px!important;width:590px!important}}.t305{{padding-left:10px!important}}.t306{{font-size:14px!important}}.t308{{mso-line-height-alt:6px!important;line-height:6px!important}}.t310{{padding-left:10px!important;padding-bottom:16px!important;width:590px!important}}.t315{{padding-left:10px!important;padding-bottom:16px!important}}.t320{{padding-left:10px!important;padding-bottom:0!important;width:590px!important}}.t325{{padding-left:10px!important;padding-bottom:0!important}}.t327{{mso-line-height-alt:12px!important;line-height:12px!important}}.t330{{padding-left:10px!important;width:590px!important}}.t335{{padding-left:10px!important}}.t336{{font-size:14px!important}}.t339{{mso-line-height-alt:0px!important;line-height:0!important;display:none!important}}.t342,.t350{{width:499px!important}}
}}
</style>
<style type="text/css">
[style*="Albert Sans"] {{font-family: 'Albert Sans', BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif !important;}}
</style>
<style type="text/css" media="screen and (min-width:481px)">.moz-text-html .t3{{mso-line-height-alt:45px!important;line-height:45px!important;display:block!important}}.moz-text-html .t9{{padding-left:50px!important;padding-bottom:37px!important;padding-right:50px!important}}.moz-text-html .t11{{padding-left:50px!important;padding-bottom:37px!important;padding-right:50px!important;width:500px!important}}.moz-text-html .t15{{padding-bottom:15px!important;width:600px!important}}.moz-text-html .t20{{padding-bottom:15px!important}}.moz-text-html .t21{{line-height:26px!important;letter-spacing:-1.56px!important}}.moz-text-html .t28{{padding:48px 50px 39px!important}}.moz-text-html .t30{{padding:48px 50px 39px!important;width:500px!important}}.moz-text-html .t34{{width:600px!important}}.moz-text-html .t44{{padding-bottom:44px!important;width:800px!important}}.moz-text-html .t49{{padding-bottom:44px!important}}.moz-text-html .t74{{width:600px!important}}.moz-text-html .t84{{width:800px!important}}.moz-text-html .t94,.moz-text-html .t99{{padding-bottom:1px!important}}.moz-text-html .t113,.moz-text-html .t123,.moz-text-html .t134{{width:600px!important}}.moz-text-html .t141{{mso-line-height-alt:0px!important;line-height:0!important;display:none!important}}.moz-text-html .t144{{width:600px!important}}.moz-text-html .t151{{mso-line-height-alt:0px!important;line-height:0!important;display:none!important}}.moz-text-html .t152{{mso-line-height-alt:18px!important;line-height:18px!important}}.moz-text-html .t154,.moz-text-html .t162{{width:488px!important}}.moz-text-html .t169{{background-color:#f8f8f8!important;padding:20px!important}}.moz-text-html .t171{{background-color:#f8f8f8!important;padding:20px!important;width:560px!important}}.moz-text-html .t175{{padding:20px 15px!important;width:570px!important}}.moz-text-html .t180{{padding:20px 15px!important}}.moz-text-html .t187{{max-width:310px!important}}.moz-text-html .t188{{padding-left:5px!important;padding-right:5px!important}}.moz-text-html .t195{{max-width:310px!important}}.moz-text-html .t196{{padding-left:5px!important;padding-right:5px!important}}.moz-text-html .t204{{max-width:600px!important}}.moz-text-html .t213{{width:600px!important}}.moz-text-html .t226{{padding-top:20px!important}}.moz-text-html .t228{{padding-top:20px!important;width:560px!important}}.moz-text-html .t232{{width:600px!important}}.moz-text-html .t242{{max-width:800px!important}}.moz-text-html .t251{{padding-left:10px!important;width:590px!important}}.moz-text-html .t256{{padding-left:10px!important}}.moz-text-html .t257{{font-size:14px!important}}.moz-text-html .t259{{mso-line-height-alt:11px!important;line-height:11px!important}}.moz-text-html .t261{{padding-left:10px!important;padding-bottom:16px!important;width:171px!important}}.moz-text-html .t266{{padding-left:10px!important;padding-bottom:16px!important}}.moz-text-html .t268{{mso-line-height-alt:9px!important;line-height:9px!important}}.moz-text-html .t271{{padding-left:10px!important;width:590px!important}}.moz-text-html .t276{{padding-left:10px!important}}.moz-text-html .t277{{font-size:14px!important}}.moz-text-html .t281{{padding-left:10px!important;padding-bottom:0!important;width:590px!important}}.moz-text-html .t286{{padding-left:10px!important;padding-bottom:0!important}}.moz-text-html .t291{{max-width:800px!important}}.moz-text-html .t300{{padding-left:10px!important;width:590px!important}}.moz-text-html .t305{{padding-left:10px!important}}.moz-text-html .t306{{font-size:14px!important}}.moz-text-html .t308{{mso-line-height-alt:6px!important;line-height:6px!important}}.moz-text-html .t310{{padding-left:10px!important;padding-bottom:16px!important;width:590px!important}}.moz-text-html .t315{{padding-left:10px!important;padding-bottom:16px!important}}.moz-text-html .t320{{padding-left:10px!important;padding-bottom:0!important;width:590px!important}}.moz-text-html .t325{{padding-left:10px!important;padding-bottom:0!important}}.moz-text-html .t327{{mso-line-height-alt:12px!important;line-height:12px!important}}.moz-text-html .t330{{padding-left:10px!important;width:590px!important}}.moz-text-html .t335{{padding-left:10px!important}}.moz-text-html .t336{{font-size:14px!important}}.moz-text-html .t339{{mso-line-height-alt:0px!important;line-height:0!important;display:none!important}}.moz-text-html .t342,.moz-text-html .t350{{width:499px!important}}</style>
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css2?family=Albert+Sans:wght@400;500;700;800&amp;display=swap" rel="stylesheet" type="text/css" />
<!--<![endif]-->
<!--[if mso]>
<style type="text/css">
div.t3{{mso-line-height-alt:45px !important;line-height:45px !important;display:block !important}}td.t9{{padding-left:50px !important;padding-bottom:37px !important;padding-right:50px !important}}td.t11{{padding-left:50px !important;padding-bottom:37px !important;padding-right:50px !important;width:600px !important}}td.t15{{padding-bottom:15px !important;width:600px !important}}td.t20{{padding-bottom:15px !important}}h1.t21{{line-height:26px !important;letter-spacing:-1.56px !important}}td.t28{{padding:48px 50px 39px !important}}td.t30{{padding:48px 50px 39px !important;width:600px !important}}td.t34{{width:600px !important}}td.t44{{padding-bottom:44px !important;width:800px !important}}td.t49{{padding-bottom:44px !important}}td.t74{{width:600px !important}}td.t84{{width:800px !important}}td.t94,td.t99{{padding-bottom:1px !important}}td.t113,td.t123,td.t134{{width:600px !important}}div.t141{{mso-line-height-alt:0px !important;line-height:0 !important;display:none !important}}td.t144{{width:600px !important}}div.t151{{mso-line-height-alt:0px !important;line-height:0 !important;display:none !important}}div.t152{{mso-line-height-alt:18px !important;line-height:18px !important}}td.t154,td.t162{{width:488px !important}}td.t169{{background-color:#f8f8f8 !important;padding:20px !important}}td.t171{{background-color:#f8f8f8 !important;padding:20px !important;width:600px !important}}td.t175{{padding:20px 15px !important;width:600px !important}}td.t180{{padding:20px 15px !important}}div.t187{{max-width:310px !important}}div.t188{{padding-left:5px !important;padding-right:5px !important}}div.t195{{max-width:310px !important}}div.t196{{padding-left:5px !important;padding-right:5px !important}}div.t204{{max-width:600px !important}}td.t209,td.t213{{width:600px !important}}td.t226{{padding-top:20px !important}}td.t228{{padding-top:20px !important;width:600px !important}}td.t232{{width:600px !important}}div.t242{{max-width:800px !important}}td.t247{{width:800px !important}}td.t251{{padding-left:10px !important;width:600px !important}}td.t256{{padding-left:10px !important}}h1.t257{{font-size:14px !important}}div.t259{{mso-line-height-alt:11px !important;line-height:11px !important}}td.t261,td.t266{{padding-left:10px !important;padding-bottom:16px !important}}div.t268{{mso-line-height-alt:9px !important;line-height:9px !important}}td.t271{{padding-left:10px !important;width:600px !important}}td.t276{{padding-left:10px !important}}h1.t277{{font-size:14px !important}}td.t281{{padding-left:10px !important;padding-bottom:0 !important;width:600px !important}}td.t286{{padding-left:10px !important;padding-bottom:0 !important}}div.t291{{max-width:800px !important}}td.t296{{width:800px !important}}td.t300{{padding-left:10px !important;width:600px !important}}td.t305{{padding-left:10px !important}}h1.t306{{font-size:14px !important}}div.t308{{mso-line-height-alt:6px !important;line-height:6px !important}}td.t310{{padding-left:10px !important;padding-bottom:16px !important;width:600px !important}}td.t315{{padding-left:10px !important;padding-bottom:16px !important}}td.t320{{padding-left:10px !important;padding-bottom:0 !important;width:600px !important}}td.t325{{padding-left:10px !important;padding-bottom:0 !important}}div.t327{{mso-line-height-alt:12px !important;line-height:12px !important}}td.t330{{padding-left:10px !important;width:600px !important}}td.t335{{padding-left:10px !important}}h1.t336{{font-size:14px !important}}div.t339{{mso-line-height-alt:0px !important;line-height:0 !important;display:none !important}}td.t342,td.t350{{width:499px !important}}
</style>
<![endif]-->
<!--[if mso]>
<xml>
<o:OfficeDocumentSettings>
<o:AllowPNG/>
<o:PixelsPerInch>96</o:PixelsPerInch>
</o:OfficeDocumentSettings>
</xml>
<![endif]-->
</head>
<body class="t0" style="min-width:100%;Margin:0px;padding:0px;background-color:#242424;"><div class="t1" style="background-color:#242424;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td class="t2" style="font-size:0;line-height:0;mso-line-height-rule:exactly;background-color:#242424;" valign="top" align="center">
<!--[if mso]>
<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
<v:fill color="#242424"/>
</v:background>
<![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center" id="innerTable"><tr><td><div class="t3" style="mso-line-height-rule:exactly;font-size:1px;display:none;">&nbsp;</div></td></tr><tr><td>
<table class="t10" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t11" style="background-color:#F8F8F8;width:420px;padding:0 30px 9px 30px;">
<!--<![endif]-->
<!--[if mso]><td class="t11" style="background-color:#F8F8F8;width:480px;padding:0 30px 9px 30px;"><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t83" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t84" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t84" style="width:480px;"><![endif]-->
<div class="t90" style="display:inline-table;width:100%;text-align:right;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="right" valign="top" width="450"><tr><td width="370" valign="top"><![endif]-->
<div class="t104" style="display:inline-table;text-align:initial;vertical-align:inherit;width:82.22222%;max-width:370px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t106"><tr>
<td class="t107" style="padding:35px 0 0 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t122" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t123" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t123" style="width:480px;"><![endif]-->
<p class="t129" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:22px;font-weight:500;font-style:normal;font-size:14px;text-decoration:none;text-transform:none;letter-spacing:-0.56px;direction:ltr;color:#333333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;"><span class="t130" style="margin:0;Margin:0;font-weight:bold;mso-line-height-rule:exactly;">Confirmation de votre réservation</span></p></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</div>
<!--[if mso]>
</td><td width="80" valign="top"><![endif]-->
<div class="t96" style="display:inline-table;text-align:initial;vertical-align:inherit;width:17.77778%;max-width:80px;"><div class="t91" style="mso-line-height-rule:exactly;mso-line-height-alt:16px;line-height:16px;font-size:1px;display:block;">&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t98"><tr>
<td class="t99" style="background-color:#F8F8F8;padding:0 0 50px 0;"><div style="font-size:0px;"><img class="t100" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="80" height="57.671875" alt="" src="https://d8e1d1ea-89a7-4860-8f1f-d3761a40c1b6.b-cdn.net/e/e3a357cf-f23c-434e-89a1-85b1dc72b475/69fdb2f9-1411-43a8-97a7-51087fcfe9cf.png"/></div></td>
</tr></table>
</div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td><div class="t12" style="mso-line-height-rule:exactly;mso-line-height-alt:25px;line-height:25px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t14" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t15" style="width:480px;padding:0 0 20px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t15" style="width:480px;padding:0 0 20px 0;"><![endif]-->
<h1 class="t21" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:28px;font-weight:800;font-style:normal;font-size:17px;text-decoration:none;text-transform:none;letter-spacing:-1.04px;direction:ltr;color:#191919;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">Bonjour {reservation_name},</h1></td>
</tr></table>
</td></tr><tr><td>
<table class="t133" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t134" style="width:480px;padding:0 0 22px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t134" style="width:480px;padding:0 0 22px 0;"><![endif]-->
<p class="t140" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:22px;font-weight:500;font-style:normal;font-size:14px;text-decoration:none;text-transform:none;letter-spacing:-0.56px;direction:ltr;color:#333333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;">Nous avons bien reçu votre réservation et nous vous attendons avec impatiente :</p></td>
</tr></table>
</td></tr><tr><td>
<table class="t170" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t171" style="background-color:#F0F0F0;width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t171" style="background-color:#F0F0F0;width:480px;"><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t174" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t175" style="background-color:#F0F0F0;width:336px;padding:0 2px 3px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t175" style="background-color:#F0F0F0;width:338px;padding:0 2px 3px 0;"><![endif]-->
<div class="t181" style="display:inline-table;width:100%;text-align:left;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top" width="430"><tr><td class="t186" style="width:5px;" width="5"></td><td width="205" valign="top"><![endif]-->
<div class="t187" style="display:inline-table;text-align:initial;vertical-align:inherit;width:50%;max-width:300px;"><div class="t188">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t189"><tr>
<td class="t190"><div class="t191" style="display:inline-table;width:100%;text-align:left;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top" width="205"><tr><td width="205" valign="top"><![endif]-->
<div class="t204" style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:480px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t206"><tr>
<td class="t207" style="padding:20px 20px 20px 20px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t212" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t213" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t213" style="width:480px;"><![endif]-->
<div class="t219" style="display:inline-table;width:100%;text-align:left;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top" width="165"><tr><td width="165" valign="top"><![endif]-->
<div class="t242" style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:480px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t244"><tr>
<td class="t245"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t250" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t251" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t251" style="width:480px;"><![endif]-->
<h1 class="t257" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:700;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">DATE</h1></td>
</tr></table>
</td></tr><tr><td><div class="t249" style="mso-line-height-rule:exactly;mso-line-height-alt:10px;line-height:10px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t260" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t261" style="border-bottom:1px solid #D6D6D6;width:181px;padding:0 0 9px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t261" style="border-bottom:1px solid #D6D6D6;width:181px;padding:0 0 9px 0;"><![endif]-->
<h1 class="t267" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">{reservation_date}</h1></td>
</tr></table>
</td></tr><tr><td><div class="t259" style="mso-line-height-rule:exactly;mso-line-height-alt:7px;line-height:7px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td><div class="t268" style="mso-line-height-rule:exactly;mso-line-height-alt:4px;line-height:4px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t270" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t271" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t271" style="width:480px;"><![endif]-->
<h1 class="t277" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:700;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">Nombre de PERSONNES</h1></td>
</tr></table>
</td></tr><tr><td><div class="t269" style="mso-line-height-rule:exactly;mso-line-height-alt:10px;line-height:10px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t280" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t281" style="width:480px;padding:0 0 13px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t281" style="width:480px;padding:0 0 13px 0;"><![endif]-->
<h1 class="t287" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">{head_count}</h1></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t186" style="width:5px;" width="5"></td><td class="t194" style="width:5px;" width="5"></td><td width="205" valign="top"><![endif]-->
<div class="t195" style="display:inline-table;text-align:initial;vertical-align:inherit;width:50%;max-width:300px;"><div class="t196">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t197"><tr>
<td class="t198"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t227" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t228" style="width:440px;padding:21px 20px 20px 20px;">
<!--<![endif]-->
<!--[if mso]><td class="t228" style="width:480px;padding:21px 20px 20px 20px;"><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t231" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t232" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t232" style="width:480px;"><![endif]-->
<div class="t238" style="display:inline-table;width:100%;text-align:left;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top" width="165"><tr><td width="165" valign="top"><![endif]-->
<div class="t291" style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:480px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t293"><tr>
<td class="t294"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t299" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t300" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t300" style="width:480px;"><![endif]-->
<h1 class="t306" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:700;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">HEURE</h1></td>
</tr></table>
</td></tr><tr><td><div class="t298" style="mso-line-height-rule:exactly;mso-line-height-alt:10px;line-height:10px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t309" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t310" style="border-bottom:1px solid #D6D6D6;width:480px;padding:0 0 9px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t310" style="border-bottom:1px solid #D6D6D6;width:480px;padding:0 0 9px 0;"><![endif]-->
<h1 class="t316" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">{reservation_time}</h1></td>
</tr></table>
</td></tr><tr><td><div class="t308" style="mso-line-height-rule:exactly;mso-line-height-alt:7px;line-height:7px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td><div class="t327" style="mso-line-height-rule:exactly;mso-line-height-alt:3px;line-height:3px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t329" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t330" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t330" style="width:480px;"><![endif]-->
<h1 class="t336" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:700;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">numéro de téléphone</h1></td>
</tr></table>
</td></tr><tr><td><div class="t328" style="mso-line-height-rule:exactly;mso-line-height-alt:10px;line-height:10px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t319" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t320" style="width:480px;padding:0 0 12px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t320" style="width:480px;padding:0 0 12px 0;"><![endif]-->
<h1 class="t326" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">{phone_number}</h1></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t194" style="width:5px;" width="5"></td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</td></tr>
<!--[if !mso]><!--><tr><td><div class="t141" style="mso-line-height-rule:exactly;mso-line-height-alt:24px;line-height:24px;font-size:1px;display:block;">&nbsp;</div></td></tr>
<!--<![endif]-->
<tr><td>
<table class="t143" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t144" style="width:480px;padding:0 0 22px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t144" style="width:480px;padding:0 0 22px 0;"><![endif]-->
<p class="t150" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:22px;font-weight:500;font-style:normal;font-size:14px;text-decoration:none;text-transform:none;letter-spacing:-0.56px;direction:ltr;color:#333333;text-align:center;mso-line-height-rule:exactly;mso-text-raise:2px;"><span class="t338" style="margin:0;Margin:0;font-weight:700;mso-line-height-rule:exactly;">Si vous avez des questions, n&#39;hésitez pas à nous contacter au 04.67.22.56.59</span></p></td>
</tr></table>
</td></tr><tr><td>
<table class="t112" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t113" style="width:368px;padding:0 0 22px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t113" style="width:368px;padding:0 0 22px 0;"><![endif]-->
<p class="t119" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:22px;font-weight:500;font-style:normal;font-size:14px;text-decoration:none;text-transform:none;letter-spacing:-0.56px;direction:ltr;color:#333333;text-align:center;mso-line-height-rule:exactly;mso-text-raise:2px;">Merci de choisir le Restaurant Nuances. À très vite !</p></td>
</tr></table>
</td></tr>
<!--[if !mso]><!--><tr><td><div class="t151" style="mso-line-height-rule:exactly;mso-line-height-alt:6px;line-height:6px;font-size:1px;display:block;">&nbsp;</div></td></tr>
<!--<![endif]-->
<tr><td>
<table class="t153" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t154" style="background-color:#181818;overflow:hidden;width:353px;text-align:center;line-height:44px;mso-line-height-rule:exactly;mso-text-raise:10px;border-radius:44px 44px 44px 44px;">
<!--<![endif]-->
<!--[if mso]><td class="t154" style="background-color:#181818;overflow:hidden;width:353px;text-align:center;line-height:44px;mso-line-height-rule:exactly;mso-text-raise:10px;border-radius:44px 44px 44px 44px;"><![endif]-->
<a class="t160" href="{booking_app_url}" style="display:block;margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:44px;font-weight:800;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;letter-spacing:2.4px;direction:ltr;color:#F8F8F8;text-align:center;mso-line-height-rule:exactly;mso-text-raise:10px;" target="_blank">faire une nouvelle réservation</a></td>
</tr></table>
</td></tr><tr><td><div class="t152" style="mso-line-height-rule:exactly;mso-line-height-alt:4px;line-height:4px;font-size:1px;display:block;">&nbsp;</div></td></tr>
<!--[if !mso]><!--><tr><td><div class="t339" style="mso-line-height-rule:exactly;mso-line-height-alt:6px;line-height:6px;font-size:1px;display:block;">&nbsp;</div></td></tr>
<!--<![endif]-->
<tr><td>
<table class="t341" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t342" style="background-color:#C20606;overflow:hidden;width:353px;text-align:center;line-height:44px;mso-line-height-rule:exactly;mso-text-raise:10px;border-radius:44px 44px 44px 44px;">
<!--<![endif]-->
<!--[if mso]><td class="t342" style="background-color:#C20606;overflow:hidden;width:353px;text-align:center;line-height:44px;mso-line-height-rule:exactly;mso-text-raise:10px;border-radius:44px 44px 44px 44px;"><![endif]-->
<a class="t348" href="{booking_app_remove_reservation_url}" style="display:block;margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:44px;font-weight:800;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;letter-spacing:2.4px;direction:ltr;color:#F8F8F8;text-align:center;mso-line-height-rule:exactly;mso-text-raise:10px;" target="_blank">supprimer la réservation</a></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</td></tr><tr><td>
<table class="t29" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t30" style="background-color:#242424;width:420px;padding:40px 30px 40px 30px;">
<!--<![endif]-->
<!--[if mso]><td class="t30" style="background-color:#242424;width:480px;padding:40px 30px 40px 30px;"><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t33" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t34" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t34" style="width:480px;"><![endif]-->
<p class="t40" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:22px;font-weight:800;font-style:normal;font-size:18px;text-decoration:none;text-transform:none;letter-spacing:-0.9px;direction:ltr;color:#757575;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;"><span class="t337" style="margin:0;Margin:0;mso-line-height-rule:exactly;">Suivez l&#39;actualité</span> du restaurant Nuances</p></td>
</tr></table>
</td></tr><tr><td>
<table class="t43" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t44" style="width:480px;padding:10px 0 36px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t44" style="width:480px;padding:10px 0 36px 0;"><![endif]-->
<div class="t50" style="display:inline-table;width:100%;text-align:center;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="center" valign="top" width="88"><tr><td class="t65" style="width:10px;" width="10"></td><td width="24" valign="top"><![endif]-->
<div class="t66" style="display:inline-table;text-align:initial;vertical-align:inherit;width:50%;max-width:44px;"><div class="t67" style="padding:0 10px 0 10px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t68"><tr>
<td class="t69"><a href="https://www.facebook.com/RestaurantNuances/?locale=fr_FR" style="font-size:0px;" target="_blank"><img class="t70" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="24" height="24" alt="" src="https://d8e1d1ea-89a7-4860-8f1f-d3761a40c1b6.b-cdn.net/e/e3a357cf-f23c-434e-89a1-85b1dc72b475/99ed315f-8eff-46a2-aaf5-130117a60a4f.png"/></a></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t65" style="width:10px;" width="10"></td><td class="t55" style="width:10px;" width="10"></td><td width="24" valign="top"><![endif]-->
<div class="t56" style="display:inline-table;text-align:initial;vertical-align:inherit;width:50%;max-width:44px;"><div class="t57" style="padding:0 10px 0 10px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t58"><tr>
<td class="t59"><a href="https://www.instagram.com/restaurantnuances/?hl=fr" style="font-size:0px;" target="_blank"><img class="t60" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="24" height="24" alt="" src="https://d8e1d1ea-89a7-4860-8f1f-d3761a40c1b6.b-cdn.net/e/e3a357cf-f23c-434e-89a1-85b1dc72b475/910545a3-cc4c-4fd3-afdf-b489a9c47379.png"/></a></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t55" style="width:10px;" width="10"></td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td>
<table class="t73" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t74" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t74" style="width:480px;"><![endif]-->
<p class="t80" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:22px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:none;direction:ltr;color:#888888;text-align:center;mso-line-height-rule:exactly;mso-text-raise:3px;">317, rue Saint-Exupéry 34130 Mauguio | 04.67.22.56.59</p></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</td></tr></table></td></tr></table></div></body>
</html>
    """