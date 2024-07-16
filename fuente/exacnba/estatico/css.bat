@echo off
COPY /B /V /Y .\css\base.css .\min-css
FOR %%i IN (./css/*.css) DO npx lightningcss --minify --bundle --targets ">= 0.25%% and last 25 versions" ./css/%%i -o ./min-css/%%i