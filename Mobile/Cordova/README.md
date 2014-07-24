
#Cordova

[Apache CORDOVA](http://cordova.apache.org/)

> Apache Cordova is a set of device APIs that allow a mobile app developer to access native device function such as the camera or accelerometer from JavaScript. Combined with a UI framework such as jQuery Mobile or Dojo Mobile or Sencha Touch, this allows a smartphone app to be developed with just HTML, CSS, and JavaScript.

Emulate smartphone [here](http://emulate.phonegap.com/)

##Test InApp Purchase

1. Download the [PayPal iOS SDK](https://github.com/paypal/PayPal-iOS-SDK).
2. Download the [PayPal Android SDK] (https://github.com/paypal/PayPal-Android-SDK).
3. Follow the official [Cordova](https://cordova.apache.org) documentation to install command line tools and create a project.
4. Run `cordova plugin add https://github.com/paypal/PayPal-Cordova-Plugin`.
5. Run `cordova platform add ios` or/and `cordova platform add android`.
6. For iOS, open the Xcode project in the `platforms/ios` folder and add the `PayPalMobile` folder from step 1.
7. For Android, copy the `libs` folder from step 2 to the `libs` folder in `platforms/android`.
8. Run `cordova build` to build the projects for all of the platforms.

[Source: PayPal](https://github.com/paypal/PayPal-Cordova-Plugin)