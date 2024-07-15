@echo off
COPY /B /V /Y .\css\base.css .\css\min-css
FOR %%i IN (./css/*.css) DO npx lightningcss --minify --bundle --targets ">= 0.25%% and last 25 versions" ./css/%%i -o ./css/min-css/%%i