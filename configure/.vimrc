filetype plugin indent on
autocmd FileType python setlocal et sta sw=4 sts=4

set autoindent " same level indent
set smartindent " next level indent
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set backspace=indent,eol,start
set hlsearch "打开高亮搜索

"set fenc=GB18030 "设定默认解码 
"set fencs=utf-8,usc-bom,euc-jp,gb18030,gbk,gb2312,cp936 
set nocp "或者 set nocompatible 用于关闭VI的兼容模式 
set number "显示行号 
set ai "或者 set autoindent vim使用自动对齐，也就是把当前行的对齐格式应用到下一行 
set si "或者 set smartindent 依据上面的对齐格式，智能的选择对齐方式
set tabstop=4 "设置tab键为4个空格
set sw=4 "或者 set shiftwidth 设置当行之间交错时使用4个空格
set ruler "设置在编辑过程中,于右下角显示光标位置的状态行 
set incsearch "设置增量搜索,这样的查询比较smart 
set showmatch "高亮显示匹配的括号 
set matchtime=5 "匹配括号高亮时间(单位为 1/10 s) set ignorecase "在搜索的时候忽略大小写 
syntax on "高亮语法


let Tlist_Show_One_File=1                                                                                                                 
let Tlist_Exit_OnlyWindow=1                                                                                                                                                  
let g:winManagerWindowLayout='FileExplorer|TagList'                                                                                                                         
nmap wm :WMToggle<cr> 
