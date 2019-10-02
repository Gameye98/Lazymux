lzmFolder = app.GetPrivateFolder("data");
function OnStart()
{
	app.MakeFolder("/sdcard/Lazymux");
	app.MakeFolder("/sdcard/Lazymux/Download");
	
	lzmcoreTask();
	app.SetOrientation( "Portrait" );
	
	layMain = app.CreateLayout( "Linear", "VCenter,FillXY" );
	layMain.SetBackColor( "black" );
	
	actionbar = app.CreateText("Lazymux", 1, 0.1, "Monospace,Center");
	actionbar.SetFontFile("FSEX300.ttf");
	actionbar.SetTextColor("black");
	actionbar.SetBackColor("white");
	actionbar.SetTextSize("45");
	layMain.AddChild(actionbar);
	
	main = app.CreateLayout("linear", "VCenter,FillXY");
	layMain.AddChild(main);
	
	checkUpdate = app.CreateButton("Check Update", 1.0, -0.05, "Custom");
	checkUpdate.SetStyle("black","black",2.0,"white",1.0);
	checkUpdate.SetOnTouch(checkUpdate_OnTouch);
	main.AddChild(checkUpdate);
	
	shareLazymux = app.CreateButton("Share Lazymux", 1.0, -0.05, "Custom");
	shareLazymux.SetStyle("black","black",2.0,"white",1.0);
	shareLazymux.SetOnTouch(shareLazymux_OnTouch);
	main.AddChild(shareLazymux);
	
	bhsBlog = app.CreateButton("BlackHole Security Blog", 1.0, -0.05, "Custom");
	bhsBlog.SetStyle("black","black",2.0,"white",1.0);
	bhsBlog.SetOnTouch(bhsBlog_OnTouch);
	main.AddChild(bhsBlog);
	
	CreateDrawer();
	
	loadPkg = app.CreateLayout("linear", "VCenter,FillXY");
	loadPkg.SetBackColor("black");
	loadPkg.SetVisibility("Hide");
	
	actionbar = app.CreateText("Lazymux", 1, 0.1, "Monospace,Center");
	actionbar.SetFontFile("FSEX300.ttf");
	actionbar.SetTextColor("black");
	actionbar.SetBackColor("white");
	actionbar.SetTextSize("45");
	loadPkg.AddChild(actionbar);
	
	dlLay = app.CreateLayout("linear","VCenter,FillXY");
	dlLay.SetBackColor("black");
	loadPkg.AddChild(dlLay);
	
	dlScroll = app.CreateScroller(1,0.9);
	dlScroll.SetBackColor("black");
	dlLay.AddChild(dlScroll);
	
	dlPkg = app.CreateLayout("linear", "VCenter,FillXY");
	dlScroll.AddChild(dlPkg);
	
	beanshell = app.CreateButton("beanshell 2.04", 1.0, -0.05, "Custom");
	beanshell.SetStyle("black","black",2.0,"white",1.0);
	beanshell.SetOnTouch(beanshell_OnTouch);
	dlPkg.AddChild(beanshell);
	
	textr = app.CreateButton("textr 1.0", 1.0, -0.05, "Custom");
	textr.SetStyle("black","black",2.0,"white",1.0);
	textr.SetOnTouch(textr_OnTouch);
	dlPkg.AddChild(textr);
	
	apsca = app.CreateButton("apsca 0.1", 1.0, -0.05, "Custom");
	apsca.SetStyle("black","black",2.0,"white",1.0);
	apsca.SetOnTouch(apsca_OnTouch);
	dlPkg.AddChild(apsca);
	
	amox = app.CreateButton("amox 1.0", 1.0, -0.05, "Custom");
	amox.SetStyle("black","black",2.0,"white",1.0);
	amox.SetOnTouch(amox_OnTouch);
	dlPkg.AddChild(amox);
	
	html = app.CreateButton("html 0.1", 1.0, -0.05, "Custom");
	html.SetStyle("black","black",2.0,"white",1.0);
	html.SetOnTouch(html_OnTouch);
	dlPkg.AddChild(html);
	
	jadx = app.CreateButton("jadx 0.6.1", 1.0, -0.05, "Custom");
	jadx.SetStyle("black","black",2.0,"white",1.0);
	jadx.SetOnTouch(jadx_OnTouch);
	dlPkg.AddChild(jadx);
	
	ginf = app.CreateButton("ginf 1.0", 1.0, -0.05, "Custom");
	ginf.SetStyle("black","black",2.0,"white",1.0);
	ginf.SetOnTouch(ginf_OnTouch);
	dlPkg.AddChild(ginf);
	
	f4k3 = app.CreateButton("f4k3 1.0", 1.0, -0.05, "Custom");
	f4k3.SetStyle("black","black",2.0,"white",1.0);
	f4k3.SetOnTouch(f4k3_OnTouch);
	dlPkg.AddChild(f4k3);
	
	inther = app.CreateButton("inther 0.1", 1.0, -0.05, "Custom");
	inther.SetStyle("black","black",2.0,"white",1.0);
	inther.SetOnTouch(inther_OnTouch);
	dlPkg.AddChild(inther);
	
	tricksTips = app.CreateLayout("linear", "VCenter,FillXY");
	tricksTips.SetBackground("black");
	tricksTips.SetVisibility("Hide");
	
	actionbar = app.CreateText("Lazymux", 1, 0.1, "Monospace,Center");
	actionbar.SetFontFile("FSEX300.ttf");
	actionbar.SetTextColor("black");
	actionbar.SetBackColor("white");
	actionbar.SetTextSize("45");
	tricksTips.AddChild(actionbar);
	
	trTips = app.CreateLayout("linear", "VCenter,FillXY");
	tricksTips.AddChild(trTips);
	
	trScroll = app.CreateScroller(1,0.9);
	trScroll.SetBackColor("black");
	trTips.AddChild(trScroll);
	
	tricksTp = app.CreateLayout("linear", "VCenter,FillXY");
	trScroll.AddChild(tricksTp);
	
	hide_cursor=app.CreateButton("<b>Hide cursor</b><br><br>$ tput civis", 1.0, 0.2, "Html,Custom");
	hide_cursor.SetStyle("black","black",2.0,"white",1.0);
	hide_cursor.SetOnTouch(hide_cursor_OnTouch);
	tricksTp.AddChild(hide_cursor);
	
	show_cursor=app.CreateButton("<b>Show cursor</b><br><br>$ tput cnorm", 1.0, 0.2, "Html,Custom");
	show_cursor.SetStyle("black","black",2.0,"white",1.0);
	show_cursor.SetOnTouch(show_cursor_OnTouch);
	tricksTp.AddChild(show_cursor);
	
	change_font_style=app.CreateButton("<b>Change Font Style</b><br><br>Change font style at: $HOME/.termux/font.ttf", 1.0, 0.2, "Html,Custom");
	change_font_style.SetStyle("black","black",2.0,"white",1.0);
	change_font_style.SetOnTouch(change_font_style_OnTouch);
	tricksTp.AddChild(change_font_style);
	
	make_stylish_prompt=app.CreateButton("<b>Make Stylish Prompt</b><br><br>PS1='\\[\\033[31m\\]root@localhost\\[\\033[0m\\]:\\[\\033[34m\\]~\\[\\033[0m\\]${PWD/$HOME}# '", 1.0, 0.2, "Html,Custom");
	make_stylish_prompt.SetStyle("black","black",2.0,"white",1.0);
	make_stylish_prompt.SetOnTouch(make_stylish_prompt_OnTouch);
	tricksTp.AddChild(make_stylish_prompt);
	
	add_action_key=app.CreateButton("<b>Add Action Key</b><br><br>Change at: $HOME/termux/.termux/termux.properties<br>extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]", 1.0, 0.2, "Html,Custom");
	add_action_key.SetStyle("black","black",2.0,"white",1.0);
	add_action_key.SetOnTouch(add_action_key_OnTouch);
	tricksTp.AddChild(add_action_key);
	
	enable_disable_action_button=app.CreateButton("<b>Enable or Disable Action Key</b><br><br>VOL UP + VOL DOWN + Q", 1.0, 0.2, "Html,Custom");
	enable_disable_action_button.SetStyle("black","black",2.0,"white",1.0);
	tricksTp.AddChild(enable_disable_action_button);
	
	get_webpage_source=app.CreateButton("<b>Get Webpage Source</b><br><br>$ lynx -dump URL > FILENAME", 1.0, 0.2, "Html,Custom");
	get_webpage_source.SetStyle("black","black",2.0,"white",1.0);
	get_webpage_source.SetOnTouch(get_webpage_source_OnTouch);
	tricksTp.AddChild(get_webpage_source);
	
	convert_pdf_txt=app.CreateButton("<b>Convert PDF to TXT</b><br><br>$ pdftotext PDF_FILE", 1.0, 0.2, "Html,Custom");
	convert_pdf_txt.SetStyle("black","black",2.0,"white",1.0);
	convert_pdf_txt.SetOnTouch(convert_pdf_txt_OnTouch);
	tricksTp.AddChild(convert_pdf_txt);
	
	display_all_hosts=app.CreateButton("<b>Display (all) hosts</b><br><br>$ arp -a", 1.0, 0.2, "Html,Custom");
	display_all_hosts.SetStyle("black","black",2.0,"white",1.0);
	display_all_hosts.SetOnTouch(display_all_hosts_OnTouch);
	tricksTp.AddChild(display_all_hosts);
	
	open_url=app.CreateButton("<b>Open URL</b><br><br>$ termux-open-url URL", 1.0, 0.2, "Html,Custom");
	open_url.SetStyle("black","black",2.0,"white",1.0);
	open_url.SetOnTouch(open_url_OnTouch);
	tricksTp.AddChild(open_url);
	
	open_file=app.CreateButton("<b>Open File</b><br><br>$ termux-open FILENAME", 1.0, 0.2, "Html,Custom");
	open_file.SetStyle("black","black",2.0,"white",1.0);
	open_file.SetOnTouch(open_file_OnTouch);
	tricksTp.AddChild(open_file);
	
	installTool = app.CreateLayout("linear", "VCenter,FillXY");
	installTool.SetBackground("black");
	installTool.SetVisibility("Hide");
	
	actionbar = app.CreateText("Lazymux", 1, 0.1, "Monospace,Center");
	actionbar.SetFontFile("FSEX300.ttf");
	actionbar.SetTextColor("black");
	actionbar.SetBackColor("white");
	actionbar.SetTextSize("45");
	installTool.AddChild(actionbar);
	
	iTool = app.CreateLayout("linear","VCenter,FillXY");
	installTool.AddChild(iTool);
	
	lzmcore = app.CreateWebView(1,0.9);
	lzmcore.SetOnProgress(lzmcore_OnProgress);
	iTool.AddChild(lzmcore);
	
	forumGroupChat = app.CreateLayout( "linear", "VCenter,FillXY" );
	forumGroupChat.SetBackColor( "black" );
	forumGroupChat.SetVisibility("hide");
	
	actionbar = app.CreateText("Lazymux", 1, 0.1, "Monospace,Center");
	actionbar.SetFontFile("FSEX300.ttf");
	actionbar.SetTextColor("black");
	actionbar.SetBackColor("white");
	actionbar.SetTextSize("45");
	forumGroupChat.AddChild(actionbar);
	
	forgrop = app.CreateLayout("linear", "VCenter,FillXY");
	forumGroupChat.AddChild(forgrop);
	
	forScroll = app.CreateScroller(1,0.9);
	forScroll.SetBackColor("black");
	forgrop.AddChild(forScroll);
	
	fgp = app.CreateLayout("linear", "VCenter,FillXY");
	fgp.SetBackColor("black");
	forScroll.AddChild(fgp);
	
	app.AddLayout( layMain );
	app.AddLayout( loadPkg );
	app.AddLayout( tricksTips );
	app.AddLayout( installTool );
	app.AddLayout( forumGroupChat );
	app.AddDrawer( drawerScroll, "Left", drawerWidth );
	
	dload = app.CreateDownloader();
	dload.SetOnComplete(dload_OnComplete);
	dload.SetOnError(dload_OnError);
	lzmcore.LoadUrl("file://"+lzmFolder+"/lzmcore.html");
	setForumGroupData();
}

//Create the drawer contents.
function CreateDrawer()
{
	//Create a layout for the drawer.
	//(Here we also put it inside a scroller to allow for long menus)
	drawerWidth = 0.75;
	drawerScroll = app.CreateScroller( drawerWidth, -1, "FillY" );
	drawerScroll.SetBackColor( "White" );
	layDrawer = app.CreateLayout( "Linear", "Left" );
	drawerScroll.AddChild( layDrawer );
	
	//Create layout for top of drawer.
	layDrawerTop = app.CreateLayout( "Absolute" );
	layDrawerTop.SetBackColor( "black" );
	layDrawerTop.SetSize( drawerWidth, 0.23 );
	layDrawer.AddChild( layDrawerTop );
	
	//Add an icon to top layout.
	var img = app.CreateImage( "logo.png", 0.30 );
	img.SetPosition( drawerWidth*0.01, 0.00 );
	layDrawerTop.AddChild( img );
	
	//Add app name to top layout.
	var txtApp = app.CreateText( "Lazymux",-1,-1,"Bold");
	txtApp.SetPosition( drawerWidth*0.07, 0.155 );
	txtApp.SetTextColor( "White" );
	txtApp.SetTextSize( 13.7, "dip" );
	layDrawerTop.AddChild( txtApp );
	
	//Add app purpose to top layout.
	txtPurpose = app.CreateText( "Termux Tool Installer");
	txtPurpose.SetPosition( drawerWidth*0.07, 0.185 );
	txtPurpose.SetTextColor( "#bbffffff" );
	txtPurpose.SetTextSize( 14, "dip" );
	layDrawerTop.AddChild( txtPurpose );
	
	//Create menu layout.
	var layMenu = app.CreateLayout( "Linear", "Left" );
	layDrawer.AddChild( layMenu );
	
	//Add a list to menu layout (with the menu style option).
	var listItems = "Home::[fa-home],Download Package::[fa-download],Tricks and Tips::[fa-android],Install Tool::[fa-terminal],Forum and Group Chat::[fa-users]";
	lstMenu1 = app.CreateList( listItems, drawerWidth, -1, "Menu,Expand" );
	lstMenu1.SetColumnWidths( -1, 0.35, 0.18 );
	lstMenu1.SelectItemByIndex( 0, true );
	lstMenu1.SetItemByIndex( 0, "Home" );
	lstMenu1.SetOnTouch( lstMenu_OnTouch );
	layMenu.AddChild( lstMenu1 );
	
	//Add seperator to menu layout.
	var sep = app.CreateImage( null, drawerWidth,0.001,"fix", 2,2 );
	sep.SetSize( -1, 1, "px" );
	sep.SetColor( "#cccccc" );
	layMenu.AddChild( sep );
	
	//Add title between menus.
	txtTitle = app.CreateText( "github.com/Gameye98",-1,-1,"Left");
	txtTitle.SetTextColor( "#666666" );
	txtTitle.SetMargins( 16,12,0,0, "dip" );
	txtTitle.SetTextSize( 14, "dip" );
	layMenu.AddChild( txtTitle );
	
	//Add a second list to menu layout.
	var listItems = "About::[fa-info],Contact::[fa-phone],Exit::[fa-close]";
	lstMenu2 = app.CreateList( listItems, drawerWidth, -1, "Menu,Expand" );
	lstMenu2.SetColumnWidths( -1, 0.35, 0.18 );
	lstMenu2.SetOnTouch( lstMenu_OnTouch );
	layMenu.AddChild( lstMenu2 );
}

//Handle menu item selection.
function lstMenu_OnTouch( title, body, type, index )
{
	//Close the drawer.
	app.CloseDrawer( "Left" );
	
	//Highlight the chosen menu item in the appropriate list.
	if( this==lstMenu1 ) lstMenu2.SelectItemByIndex(-1);
	else lstMenu1.SelectItemByIndex(-1);
	this.SelectItemByIndex( index, true );
	
	switch(title) {
		case "Home": layMain.SetVisibility("Show");tricksTips.SetVisibility("Hide");installTool.SetVisibility("Hide");loadPkg.SetVisibility("Hide");forumGroupChat.SetVisibility("Hide");
		break;
		case "Download Package": loadPkg.SetVisibility("Show");layMain.SetVisibility("Hide");tricksTips.SetVisibility("Hide");installTool.SetVisibility("Hide");forumGroupChat.SetVisibility("Hide");
		break;
		case "Tricks and Tips": tricksTips.SetVisibility("Show");layMain.SetVisibility("Hide");installTool.SetVisibility("Hide");loadPkg.SetVisibility("Hide");forumGroupChat.SetVisibility("Hide");
		break;
		case "Install Tool": installTool.SetVisibility("Show");tricksTips.SetVisibility("Hide");layMain.SetVisibility("Hide");loadPkg.SetVisibility("Hide");forumGroupChat.SetVisibility("Hide");
		break;
		case "Forum and Group Chat": forumGroupChat.SetVisibility("Show");layMain.SetVisibility("Hide");loadPkg.SetVisibility("Hide");installTool.SetVisibility("Hide");tricksTips.SetVisibility("Hide");
		break;
		case "About": app.Alert("Version "+app.ReadFile("version.txt")+"\n\nCopyright (C) 2019 by DedSecTL\n\nDedSecTL\nCvar1984\nCiKu370\nMr.TenSwapper07\namsitlab\n[M]izuno\n3RROR_TMX\nMr.K3N\nZetSec\nTroublemaker97\nL_Viole\nX14N23N6\nMR.R45K1N\nlord.zephyrus\n4cliba788\nmr0x100\nMrx04\nViruz\nMr_007\nITermSec\nIdannovita.\nBlackHole Security.","Lazymux");
		break;
		case "Contact": contactShow();
		break;
		case "Exit": app.Exit();
		break;
	default: void 0;
	}
}

//Called when a drawer is opened or closed.
function OnDrawer( side, state )
{
	console.log( side + " : " + state );
}

//Called when hardware menu key pressed.
function OnMenu( name )
{  
   app.OpenDrawer();
}
//Main App
function bhsBlog_OnTouch() {
	app.OpenUrl("https://blackholesec.blogspot.com");
}
//Download Package
function beanshell_OnTouch() {
	bshTo = app.CreateYesNoDialog("Package: beanshell\nVersion: 2.0b4\nMaintainer: Amsit <dezavue3@gmail.com> (original author - by Pat Niemeyer <pat@pat.net>)\nArchitecture: all\nDescription: BeanShell is a small, free, embeddable Java source interpreter with object scripting language features, written in Java\n\nDownload the package?");
	bshTo.SetOnTouch(bshTo_OnTouch);
	bshTo.Show();
}
function bshTo_OnTouch(choose) {
	if(choose == "Yes") {
		DownloadTask("https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb","/sdcard/Lazymux/Download");
	} else {
		void 0;
	}
}
function textr_OnTouch() {
	textrTo = app.CreateYesNoDialog("Package: textr\nVersion: 1.0\nArchitecture: all\nMaintainer: Amsit <dezavue3@gmail.com>\nDescription: Simple tool for running text\n\nDownload the package?");
	textrTo.SetOnTouch(textrTo_OnTouch);
	textrTo.Show();
}
function textrTo_OnTouch(choose) {
	if(choose == "Yes") {
		DownloadTask("https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb","/sdcard/Lazymux/Download");
	} else {
		void 0;
	}
}
function apsca_OnTouch() {
	apscaTo = app.CreateYesNoDialog("Package: apsca\nVersion: 0.1\nArchitecture: all\nHomepages: https://github.com/BlackHoleSecurity/apsca\nMaintainer: DedSecTL <dtlily>\nInstalled-Size: 48 KB\nDescription: Powerful web penetration application which finds admin panel, upload panel, shell, hidden file, hidden page and other sensitive information\n\nDownload the package?");
	apscaTo.SetOnTouch(apscaTo_OnTouch);
	apscaTo.Show();
}
function apscaTo_OnTouch(choose) {
	if(choose == "Yes") {
		DownloadTask("https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb","/sdcard/Lazymux/Download");
	} else {
		void 0;
	}
}
function amox_OnTouch() {
	amoxTo = app.CreateYesNoDialog("Package: amox\nVersion: 1.0\nArchitecture: all\nHomepages: https://gitlab.com/dtlily/amox\nMaintainer: DedSecTL/DTL <dtlily>\nInstalled-Size: 40 KB\nDescription: Find backdoor or shell planted on a site via dictionary attack\n\nDownload the package?");
	amoxTo.SetOnTouch(amoxTo_OnTouch);
	amoxTo.Show();
}
function amoxTo_OnTouch(choose) {
	if(choose == "Yes") {
		DownloadTask("https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb","/sdcard/Lazymux/Download");
	} else {
		void 0;
	}
}
function html_OnTouch() {
	htmlTo = app.CreateYesNoDialog("Package: jadx\nVersion: 0.6.1\nMaintainer: @Lexiie\nInstalled-Size: unknown\nHomepage: http://lexiie.web.id\nDescription: Jadx is dex to java decompiler\n\nDownload the package?");
	htmlTo.SetOnTouch(jadxTo_OnTouch);
	htmlTo.Show();
}
function htmlTo_OnTouch(choose) {
	if(choose == "Yes") {
		DownloadTask("https://raw.githubusercontent.com/Cvar1984/HPB/master/html_0.1_all.deb","/sdcard/Lazymux/Download");
	} else {
		void 0;
	}
}
function jadx_OnTouch() {
	jadxTo = app.CreateYesNoDialog("Package: jadx\nVersion: 0.6.1\nArchitecture: all\nMaintainer: @Lexiie\nHomepage: http://lexiie.web.id\nDescription: Jadx is dex to java decompiler\n\nDownload the package?");
	jadxTo.SetOnTouch(jadxTo_OnTouch);
	jadxTo.Show();
}
function jadxTo_OnTouch(choose) {
	if(choose == "Yes") {
		DownloadTask("https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true","/sdcard/Lazymux/Download");
	} else {
		void 0;
	}
}
function ginf_OnTouch() {
	ginfTo = app.CreateYesNoDialog("Package: ginf\nVersion: 1.0\nArchitecture: all\nHomepages: https://github.com/Gameye98/GINF\nMaintainer: DedSecTL <dtlily>\nDepends: php\nInstalled-Size: 12 KB\nDescription: GitHub information gathering\n\nDownload the package?");
	ginfTo.SetOnTouch(ginfTo_OnTouch);
	ginfTo.Show();
}
function ginfTo_OnTouch(choose) {
	if(choose == "Yes") {
		DownloadTask("https://github.com/Gameye98/Gameye98.github.io/blob/master/package/ginf_1.0_all.deb","/sdcard/Lazymux/Download");
	} else {
		void 0;
	}
}
function f4k3_OnTouch() {
	f4k3To = app.CreateYesNoDialog("Package: f4k3\nVersion: 1.0\nArchitecture: all\nMaintainer: DedSecTL <dtlily>\nDepends: jq, curl\nInstalled-Size: 3072 B\nDescription: Fake User Data Generator\n\nDownload the package?");
	f4k3To.SetOnTouch(f4k3To_OnTouch);
	f4k3To.Show();
}
function f4k3To_OnTouch(choose) {
	if(choose == "Yes") {
		DownloadTask("https://github.com/Gameye98/Gameye98.github.io/blob/master/package/f4k3_1.0_all.deb","/sdcard/Lazymux/Download");
	} else {
		void 0;
	}
}
function inther_OnTouch() {
	intherTo = app.CreateYesNoDialog("Package: inther\nVersion: 0.1\nArchitecture: all\nHomepages: https://github.com/Gameye98/inther\nMaintainer: DedSecTL <dtlily>\nDepends: ruby\nInstalled-Size: 16 KB\nDescription: information gathering using shodan search engine, censys and more\n\nDownload the package?");
	intherTo.SetOnTouch(intherTo_OnTouch);
	intherTo.Show();
}
function intherTo_OnTouch(choose) {
	if(choose == "Yes") {
		DownloadTask("https://github.com/Gameye98/Gameye98.github.io/blob/master/package/inther_0.1_all.deb","/sdcard/Lazymux/Download");
	} else {
		void 0;
	}
}
//Tricks and Tip
function hide_cursor_OnTouch(){app.SetClipboardText("tput civis");app.ShowPopup("Copied to clipboard!");}
function show_cursor_OnTouch(){app.SetClipboardText("tput cnorm");app.ShowPopup("Copied to clipboard!");}
function change_font_style_OnTouch(){app.SetClipboardText("$HOME/.termux/font.ttf");app.ShowPopup("Copied to clipboard!");}
function make_stylish_prompt_OnTouch(){app.SetClipboardText("PS1='\\[\\033[31m\\]root@localhost\\[\\033[0m\\]:\\[\\033[34m\\]~\\[\\033[0m\\]${PWD/$HOME}# '");app.ShowPopup("Copied to clipboard!");}
function add_action_key_OnTouch(){app.SetClipboardText("extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]");app.ShowPopup("Copied to clipboard!");}
function get_webpage_source_OnTouch(){app.SetClipboardText("lynx -dump URL > FILENAME");app.ShowPopup("Copied to clipboard!");}
function convert_pdf_txt_OnTouch(){app.SetClipboardText("pdftotext PDF_FILE");app.ShowPopup("Copied to clipboard!");}
function display_all_hosts_OnTouch(){app.SetClipboardText("arp -a");app.ShowPopup("Copied to clipboard!");}
function open_url_OnTouch(){app.SetClipboardText("termux-open-url URL");app.ShowPopup("Copied to clipboard!");}
function open_file_OnTouch(){app.SetClipboardText("termux-open FILENAME");app.ShowPopup("Copied to clipboard!");}

function Scroll() {
	scroll.ScrollTo(0,999);
	tscroll.ScrollTo(0,999);
}
function contactShow() {
	contactDlg = app.CreateDialog("Contact");
	contactDlg.SetBackColor("white");
	
	layContact = app.CreateLayout("linear", "VCenter,FillXY");
	layContact.SetSize(0.9,0.5);
	layContact.SetBackColor("#1C1C1C");
	contactDlg.AddLayout(layContact);
	
	instagram = app.CreateButton("Instagram (dtlily)", 0.9, -0.05, "Custom");
	instagram.SetStyle("black","black",2.0,"white",1.0);
	instagram.SetOnTouch(instagram_OnTouch);
	layContact.AddChild(instagram);
	
	telegram = app.CreateButton("Telegram (dtlily)", 0.9, -0.05, "Custom");
	telegram.SetStyle("black","black",2.0,"white",1.0);
	telegram.SetOnTouch(telegram_OnTouch);
	layContact.AddChild(telegram);
	
	facebook = app.CreateButton("Facebook (cgi.izo)", 0.9, -0.05, "Custom");
	facebook.SetStyle("black","black",2.0,"white",1.0);
	facebook.SetOnTouch(facebook_OnTouch);
	layContact.AddChild(facebook);
	
	github = app.CreateButton("GitHub (Gameye98)", 0.9, -0.05, "Custom");
	github.SetStyle("black","black",2.0,"white",1.0);
	github.SetOnTouch(github_OnTouch);
	layContact.AddChild(github);
	
	gitlab = app.CreateButton("GitLab (dtlily)", 0.9, -0.05, "Custom");
	gitlab.SetStyle("black","black",2.0,"white",1.0);
	gitlab.SetOnTouch(gitlab_OnTouch);
	layContact.AddChild(gitlab);
	
	youtube = app.CreateButton("Youtube (dtlily)", 0.9, -0.05, "Custom");
	youtube.SetStyle("black","black",2.0,"white",1.0);
	youtube.SetOnTouch(youtube_OnTouch);
	layContact.AddChild(youtube);
	
	contactDlg.Show();
}
function instagram_OnTouch() {
	app.OpenUrl("https://www.instagram.com/dtlily");
}
function telegram_OnTouch() {
	app.OpenUrl("https://t.me/dtlily");
}
function facebook_OnTouch() {
	app.OpenUrl("https://facebook.com/cgi.izo");
}
function github_OnTouch() {
	app.OpenUrl("https://github.com/Gameye98");
}
function gitlab_OnTouch() {
	app.OpenUrl("https://gitlab.com/dtlily");
}
function youtube_OnTouch() {
	app.OpenUrl("https://m.youtube.com/channel/UCx-ohDJBkdKzeXOGZ2hoaMA");
}
function DownloadTask(srcFileUrl, targetDir) {
	dload.Download(srcFileUrl, targetDir);
}
function dload_OnComplete() {
	app.ShowPopup("Download completed!");
}
function dload_OnError(error) {
	alert(error);
}
function lzmcore_OnProgress( progress ) {
	app.Debug( "progress = " + progress );
	if( progress==100 ) {
		app.HideProgress();
	}
}
function lzmcoreTask() {
	lzmcorePy_0 = app.ReadFile("lzmcore.py");
	lzmcorePy_1 = lzmcorePy_0.split(/Installing /g).length;
	str = "<!DOCTYPE html><html><head><title>Lazymux</title></head><body bgcolor=\"black\"><font color=\"white\"><pre>";
	for(x = 1;x < lzmcorePy_1;x++) {
		str += "Installing "+lzmcorePy_0.split(/Installing /g)[x].split(/Done/g)[0].replace(/\t/g,"").split(/print/g)[0].replace("###### ","").replace(/\n/g,"<br>").replace("'<br>os.system('","<br><font color=\"ocean\">").replace(/os.system\('/g,"<font color=\"ocean\">").replace(/'\)/g,"</font>").replace('"<br>os.system("',"<br><font color=\"ocean\">").replace(/os.system\("/g,"<font color=\"ocean\">").replace(/"\)/g,"</font>")+ "<br><br>";
	}
	str += "</pre></font></body></html>";
	app.WriteFile(lzmFolder+"/lzmcore.html",str);
}
function setForumGroupData() {
	try {
		xhr = new XMLHttpRequest();
		xhr.open("GET","https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/json/lazymux_gc.json",false);
		xhr.send();
		if(xhr.status == 200) {
			app.WriteFile(lzmFolder+"/lazymux_gc.json",xhr.response);
			data = JSON.parse(app.ReadFile(lzmFolder+"/lazymux_gc.json"));
			for(x = 0;x < data["forum"].length;x++) {
				app.SetData("forum:"+data["forum"][x]["id"],data["forum"][x]["url"]);
				eval('btn=app.CreateButton("forum:'+data["forum"][x]["name"]+'", 1.0, -0.05, "Custom");');
				eval('btn.SetStyle("black","black",2.0,"white",1.0);');
				eval('btn.SetTextColor("white");');
				eval('btn.SetOnTouch(btn_OnTouch);');
				eval('fgp.AddChild(btn);');
			}
			for(x = 0;x < data["group_chat"].length;x++) {
				if(data["group_chat"][x]["appId"] == "Telegram" || data["group_chat"][x]["appId"] == "Whatsapp") {
					app.SetData("group_chat:"+data["group_chat"][x]["id"],data["group_chat"][x]["url"]);
					str = "group_chat:"+data["group_chat"][x]["name"]+" ("+data["group_chat"][x]["appId"]+")\nadmin:"+data["group_chat"][x]["admin"];
					eval('btn=app.CreateButton(str, 1.0, -0.05, "Custom");');
				} else {
					app.SetData("group:"+data["group_chat"][x]["id"],data["group_chat"][x]["url"]);
					str = "group:"+data["group_chat"][x]["name"]+" ("+data["group_chat"][x]["appId"]+")\nadmin:"+data["group_chat"][x]["admin"];
					eval('btn=app.CreateButton(str, 1.0, -0.05, "Custom");');
				}
				eval('btn.SetStyle("black","black",2.0,"white",1.0);');
				eval('btn.SetTextColor("white");');
				eval('btn.SetOnTouch(btn_OnTouch);');
				eval('fgp.AddChild(btn);');
			}
		} else {
			if(app.FileExists(lzmFolder+"/lazymux_gc.json") != true) {
				app.WriteFile(lzmFolder+"/lazymux_gc.json",app.ReadFile("lazymux_gc.json"));
			}
		}
	} catch(e) {
		if(app.FileExists(lzmFolder+"/lazymux_gc.json") != true) {
			app.WriteFile(lzmFolder+"/lazymux_gc.json",app.ReadFile("lazymux_gc.json"));
		}
		try {
			data = JSON.parse(app.ReadFile(lzmFolder+"/lazymux_gc.json"));
			for(x = 0;x < data["forum"].length;x++) {
				app.SetData("forum:"+data["forum"][x]["id"],data["forum"][x]["url"]);
				eval('btn=app.CreateButton("forum:'+data["forum"][x]["name"]+'", 1.0, -0.05, "Custom");');
				eval('btn.SetStyle("black","black",2.0,"white",1.0);');
				eval('btn.SetTextColor("white");');
				eval('btn.SetOnTouch(btn_OnTouch);');
				eval('fgp.AddChild(btn);');
			}
			for(x = 0;x < data["group_chat"].length;x++) {
				if(data["group_chat"][x]["appId"] == "Telegram" || data["group_chat"][x]["appId"] == "Whatsapp") {
					app.SetData("group_chat:"+data["group_chat"][x]["id"],data["group_chat"][x]["url"]);
					str = "group_chat:"+data["group_chat"][x]["name"]+" ("+data["group_chat"][x]["appId"]+")\nadmin:"+data["group_chat"][x]["admin"];
					eval('btn=app.CreateButton(str, 1.0, -0.05, "Custom");');
				} else {
					app.SetData("group:"+data["group_chat"][x]["id"],data["group_chat"][x]["url"]);
					str = "group:"+data["group_chat"][x]["name"]+" ("+data["group_chat"][x]["appId"]+")\nadmin:"+data["group_chat"][x]["admin"];
					eval('btn=app.CreateButton(str, 1.0, -0.05, "Custom");');
				}
				eval('btn.SetStyle("black","black",2.0,"white",1.0);');
				eval('btn.SetTextColor("white");');
				eval('btn.SetOnTouch(btn_OnTouch);');
				eval('fgp.AddChild(btn);');
			}
		} catch(e) {
			alert("Something went error...");
		}
	}
}
function btn_OnTouch() {
	app.SetData("dlgData",this.GetText());
	if(this.GetText().match(/forum:/g)) {
		app.OpenUrl(app.GetData(this.GetText().split(" (")[0].toLowerCase().replace(/ /g,"_")));
	} else {
		dlg = app.CreateListDialog(this.GetText().split(" (")[0].split(":")[1],"Join the Group Chat,Contact the Admin");
		dlg.SetOnTouch(dlg_OnTouch);
		dlg.Show();
	}
}
function checkUpdate_OnTouch() {
	app.ShowProgress("Checking update...");
	version = app.ReadFile("version.txt");
	try {
		xhr = new XMLHttpRequest();
		xhr.open("GET","https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/version/Ieshnow",false);
		xhr.send();
		app.HideProgress();
		if(xhr.status == 200) {
			data = JSON.parse(xhr.response);
			if(data["version"] == version) {
				alert("Lazymux is already the newest version ("+version+").");
			} else {
				app.SetData("newVersion",data["url"]);
				updateNah = app.CreateYesNoDialog("A new version of Lazymux is available!\nThe version that is currently installed is : "+version+"\n\nUpdate the Lazymux?");
				updateNah.SetOnTouch(updateNah_OnTouch);
				updateNah.Show();
			}
		} else {
			alert("Something went error...");
		}
	} catch(e) {
		app.HideProgress();
		alert("Device is not connected to the internet");
	}
}
function updateNah_OnTouch(choose) {
	if(choose == "Yes") {
		app.OpenUrl(app.GetData("newVersion"));
	} else {
		void 0;
	}
}
function shareLazymux_OnTouch() {
	list = app.GetInstalledApps();
	for(x = 0;x < list.length;x++) {
		if(list[x].sourceDir.match(/sec.blackhole.lazymux/g)) {
			app.CopyFile(list[x].sourceDir, "/sdcard/Lazymux/Lazymux.apk");
		}
	}
	app.SendFile("/sdcard/Lazymux/Lazymux.apk","Lazymux.apk","Send File");
}
function dlg_OnTouch(item) {
	switch(item) {
		case "Join the Group Chat": app.OpenUrl(app.GetData(app.GetData("dlgData").split(" (")[0].toLowerCase().replace(/ /g,"_")));
		break;
		case "Contact the Admin": app.OpenUrl(app.GetData("dlgData").split("admin:")[1]);
		break;
	default: void 0;
	}
}