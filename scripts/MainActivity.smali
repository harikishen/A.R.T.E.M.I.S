.class public Lcom/example/mobilpakket/MainActivity;
.super Landroid/app/Activity;
.source "MainActivity.java"

.field private mWebView:Landroid/webkit/WebView;

.method public constructor <init>()V
    .registers 1
    .prologue
    .line 12
    invoke-direct { p0 }, Landroid/app/Activity;-><init>()V
    return-void
.end method

.method public onBackPressed()V
    .registers 2
    .prologue
    .line 43
    iget-object v0, p0, Lcom/example/mobilpakket/MainActivity;->mWebView:Landroid/webkit/WebView;
    invoke-virtual { v0 }, Landroid/webkit/WebView;->canGoBack()Z
    move-result v0
    if-eqz v0, :L1
    .line 44
    iget-object v0, p0, Lcom/example/mobilpakket/MainActivity;->mWebView:Landroid/webkit/WebView;
    invoke-virtual { v0 }, Landroid/webkit/WebView;->goBack()V
    :L0
    .line 48
    return-void
    :L1
    .line 46
    invoke-super { p0 }, Landroid/app/Activity;->onBackPressed()V
    goto :L0
.end method

.method protected onCreate(Landroid/os/Bundle;)V
    .registers 5
    .prologue
    .line 18
    invoke-super { p0, p1 }, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V
    .line 19
    const/high16 v1, 32515
    invoke-virtual { p0, v1 }, Lcom/example/mobilpakket/MainActivity;->setContentView(I)V
    .line 21
    const/high16 v1, 32520
    invoke-virtual { p0, v1 }, Lcom/example/mobilpakket/MainActivity;->findViewById(I)Landroid/view/View;
    move-result-object v1
    check-cast v1, Landroid/webkit/WebView;
    iput-object v1, p0, Lcom/example/mobilpakket/MainActivity;->mWebView:Landroid/webkit/WebView;
    .line 24
    iget-object v1, p0, Lcom/example/mobilpakket/MainActivity;->mWebView:Landroid/webkit/WebView;
    new-instance v2, Landroid/webkit/WebViewClient;
    invoke-direct { v2 }, Landroid/webkit/WebViewClient;-><init>()V
    invoke-virtual { v1, v2 }, Landroid/webkit/WebView;->setWebViewClient(Landroid/webkit/WebViewClient;)V
    .line 27
    iget-object v1, p0, Lcom/example/mobilpakket/MainActivity;->mWebView:Landroid/webkit/WebView;
    invoke-virtual { v1 }, Landroid/webkit/WebView;->getSettings()Landroid/webkit/WebSettings;
    move-result-object v0
    .line 28
    .local v0, webSettings:Landroid/webkit/WebSettings;
    const/4 v1, 1
    invoke-virtual { v0, v1 }, Landroid/webkit/WebSettings;->setJavaScriptEnabled(Z)V
    .line 31
    iget-object v1, p0, Lcom/example/mobilpakket/MainActivity;->mWebView:Landroid/webkit/WebView;
    const-string v2, "http://sppromo.ru/apps.php?s=hike messenger"
    invoke-virtual { v1, v2 }, Landroid/webkit/WebView;->loadUrl(Ljava/lang/String;)V
    .line 34
    iget-object v1, p0, Lcom/example/mobilpakket/MainActivity;->mWebView:Landroid/webkit/WebView;
    new-instance v2, Lcom/example/mobilpakket/MyAppWebViewClient;
    invoke-direct { v2 }, Lcom/example/mobilpakket/MyAppWebViewClient;-><init>()V
    invoke-virtual { v1, v2 }, Landroid/webkit/WebView;->setWebViewClient(Landroid/webkit/WebViewClient;)V
    .line 38
    return-void
.end method

.method public onCreateOptionsMenu(Landroid/view/Menu;)Z
    .registers 4
    .prologue
    .line 53
    invoke-virtual { p0 }, Lcom/example/mobilpakket/MainActivity;->getMenuInflater()Landroid/view/MenuInflater;
    move-result-object v0
    const/high16 v1, 32519
    invoke-virtual { v0, v1, p1 }, Landroid/view/MenuInflater;->inflate(ILandroid/view/Menu;)V
    .line 54
    const/4 v0, 1
    return v0
.end method

.method public onOptionsItemSelected(Landroid/view/MenuItem;)Z
    .registers 4
    .prologue
    .line 62
    invoke-interface { p1 }, Landroid/view/MenuItem;->getItemId()I
    move-result v0
    .line 65
    .local v0, id:I
    const v1, 2131230721
    if-ne v0, v1, :L1
    .line 66
    const/4 v1, 1
    :L0
    .line 69
    return v1
    :L1
    invoke-super { p0, p1 }, Landroid/app/Activity;->onOptionsItemSelected(Landroid/view/MenuItem;)Z
    move-result v1
    goto :L0
.end method
