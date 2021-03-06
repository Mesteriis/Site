
!function ($) {
	"use strict";
	
	var defaults = {
		'loginUrl' : '/',
		'className' : undefined,
		'sortable' : true,
		'resize' : undefined
	};
	
	/**
	 * 常量
	 */
	var constants = {
		closeBtnTemplate : '<button type="button" class="navTabsCloseBtn" title="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>',
		noCloseClass : 'noclose',
		noSortClass : 'noSort',
		prefixKey : 'bTabs_'
	};
	
	var bTabs = function(box,p){
		this.$container = box;
		this.openTabs = new Array();
		this.p = p;
	};

	bTabs.version = '1.0';

	bTabs.prototype.init = function(){
		var self = this,c = constants, $tabs = this.$container, openTabs = this.openTabs, p = this.p;
		
		$($tabs).addClass('bTabs');
		if(p.className) $($tabs).addClass(p.className);
		
		$('ul.nav-tabs a',$($tabs)).each(function(i,row){
			var li = $(this).closest('li');
			if(li && !$(li).hasClass(c.noCloseClass)) $(row).append(c.closeBtnTemplate);
		});
		$('div.tab-content div.tab-pane',$tabs).each(function(i,row){
			openTabs.push($(this).attr('id'));
		});
		$('ul.nav-tabs',$tabs).on('click','button',function(e){
			var id = $(this).parent().attr('href').replace('#', '');
			self.closeTab(id);
		});
		if(p.sortable && $.fn.sortable){
			$('ul.nav-tabs',$tabs).sortable({
				items : "li:not(."+c.noSortClass+")",
				cancel : "li:not(.active)",
				axis : "x",
				placeholder : 'bTabsPlaceHolder',
				forcePlaceholderSize : true,
				stop : function(e,ui){}
			}).disableSelection();
		}
		if(p && p.resize && $.isFunction(p.resize)){
			p.resize();
			self.innerResize();
			$(window).off('resize.bTabs').on('resize.bTabs',function(e){
				p.resize();
				self.innerResize();
			});
		}
	};
	bTabs.prototype.innerResize = function(){
		var $tabs = this.$container;
		var mainHeight = $($tabs).innerHeight();
		var tabBarHeight = $('ul.nav-tabs',$tabs).outerHeight(true);
		$('div.tab-content',$tabs).height(mainHeight - tabBarHeight);
	};
	bTabs.prototype.addTab = function(id,title,url,loginCheck){
		if(!id || !title || !url) console.error('error id, title, url');
		var c = constants, $tabs = this.$container, openTabs = this.openTabs, p = this.p;
		var tabId = c.prefixKey + id;
		if(openTabs && $.isArray(openTabs) && openTabs.length>0){
			var exist = false;
			$.each(openTabs,function(i,row){
				if(row == tabId){
					exist = true;
					return false;
				}
			});
			if(exist){
				$('ul.nav-tabs a[href="#'+tabId+'"]',$tabs).tab('show');
				return;
			}
		}else openTabs = new Array();
		$('ul.nav-tabs',$tabs).append('<li><a href="#'+tabId+'" data-toggle="tab">'+title+c.closeBtnTemplate+'</a></li>');
		var content = $('<div class="tab-pane" id="'+tabId+'"></div>');
		$('div.tab-content',$tabs).append(content);
		$('ul.nav-tabs li:last a',$tabs).tab('show');
		openTabs.push(tabId);
		
		var openIframe = function(){
			$(content).append('<iframe frameborder="0" scrolling="yes" style="width:100%;height:100%;border:0px;" src="'+url+'"></iframe>');
		};
		if(loginCheck && $.isFunction(loginCheck)){
			if(loginCheck()) openIframe();
			else if(p && p.loginUrl) window.top.location.replace(p.loginUrl);
		}else openIframe();
	};
	bTabs.prototype.closeTab = function(id){
		var c = constants, $tabs = this.$container, openTabs = this.openTabs;
		var thisTab = $('#' + id);
		$(thisTab).remove();
		var a = $('ul.nav-tabs a[href="#'+id+'"]',$tabs);
		var li = $(a).closest('li');
		var prevLi = $(li).prev();
		li.remove();
		if(openTabs && $.isArray(openTabs) && openTabs.length>0){
			var index = -1;
			$.each(openTabs,function(i,d){
				if(d == id){
					index = i;
					return false;
				}
			});
			if(index != -1) openTabs.splice(index,1);
		}
		if(prevLi.size() > 0 ) $('a',$(prevLi)).tab('show');
	};
	
	function Plugin(p){
		return this.each(function(){
			var $this = $(this),
				data = $this.data('bTabs'),
				params = $.extend({}, defaults, $this.data(), typeof p == 'object' && p);
			if(!data) $this.data('bTabs', (data = new bTabs(this,params)));
			data.init();
		});
	}
	
	function bTabsAdd(id,title,url,loginCheck){
		return this.each(function(){
			if(!id || !title || !url) return;
			var $this = $(this),data = $this.data('bTabs');
			if(data) data.addTab(id,title,url,loginCheck);
		});
	}

	function bTabsClose(id){
		return this.each(function(){
			if(!id || !title || !url) return;
			var $this = $(this),data = $this.data('bTabs');
			if(data) data.closeTab(id);
		});
	}
	
	var old = $.fn.bTabs;

	$.fn.bTabs             = Plugin;
	$.fn.bTabs.Constructor = bTabs;
	$.fn.bTabsAdd          = bTabsAdd;
	$.fn.bTabsClose        = bTabsClose;
	
	$.fn.bTabs.noConflict = function () {
		$.fn.bTabs = old;
		return this;
	};
}(window.jQuery);