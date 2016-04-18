var CSSParser=Editor.Parser=function(){function c(c,d){d=d||0;var e=a(c),f=!1,g=!1,h={next:function(){var a=e.next(),c=a.style,h=a.content;c=="css-identifier"&&g&&(a.style="css-value"),c=="css-hash"&&(a.style=g?"css-colorcode":"css-identifier"),h=="\n"&&(a.indentation=b(f,g,d)),h=="{"?f=!0:h=="}"?f=g=!1:f&&h==";"?g=!1:f&&c!="css-comment"&&c!="whitespace"&&(g=!0);return a},copy:function(){var b=f,c=g,d=e.state;return function(i){e=a(i,d),f=b,g=c;return h}}};return h}function b(a,b,c){return function(d){return!a||/^\}/.test(d)?c:b?c+indentUnit*2:c+indentUnit}}var a=function(){function d(b){return function(c,d){var e=!1;while(!c.endOfLine()){var f=c.next();if(f==b&&!e)break;e=!e&&f=="\\"}e||d(a);return"css-string"}}function c(b,c){var d=0;while(!b.endOfLine()){var e=b.next();if(d>=2&&e==">"){c(a);break}d=e=="-"?d+1:0}return"css-comment"}function b(b,c){var d=!1;while(!b.endOfLine()){var e=b.next();if(d&&e=="/"){c(a);break}d=e=="*"}return"css-comment"}function a(a,e){var f=a.next();if(f=="@"){a.nextWhileMatches(/\w/);return"css-at"}if(f=="/"&&a.equals("*")){e(b);return null}if(f=="<"&&a.equals("!")){e(c);return null}if(f=="=")return"css-compare";if(!a.equals("=")||f!="~"&&f!="|"){if(f=='"'||f=="'"){e(d(f));return null}if(f=="#"){a.nextWhileMatches(/\w/);return"css-hash"}if(f=="!"){a.nextWhileMatches(/[ \t]/),a.nextWhileMatches(/\w/);return"css-important"}if(/\d/.test(f)){a.nextWhileMatches(/[\w.%]/);return"css-unit"}if(/[,.+>*\/]/.test(f))return"css-select-op";if(/[;{}:\[\]]/.test(f))return"css-punctuation";a.nextWhileMatches(/[\w\\\-_]/);return"css-identifier"}a.next();return"css-compare"}return function(b,c){return tokenizer(b,c||a)}}();return{make:c,electricChars:"}"}}()