filetype plugin indent on
autocmd FileType python setlocal et sta sw=4 sts=4

set autoindent " same level indent
set smartindent " next level indent
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set backspace=indent,eol,start
set hlsearch "�򿪸�������

"set fenc=GB18030 "�趨Ĭ�Ͻ��� 
"set fencs=utf-8,usc-bom,euc-jp,gb18030,gbk,gb2312,cp936 
set nocp "���� set nocompatible ���ڹر�VI�ļ���ģʽ 
set number "��ʾ�к� 
set ai "���� set autoindent vimʹ���Զ����룬Ҳ���ǰѵ�ǰ�еĶ����ʽӦ�õ���һ�� 
set si "���� set smartindent ��������Ķ����ʽ�����ܵ�ѡ����뷽ʽ
set tabstop=4 "����tab��Ϊ4���ո�
set sw=4 "���� set shiftwidth ���õ���֮�佻��ʱʹ��4���ո�
set ruler "�����ڱ༭������,�����½���ʾ���λ�õ�״̬�� 
set incsearch "������������,�����Ĳ�ѯ�Ƚ�smart 
set showmatch "������ʾƥ������� 
set matchtime=5 "ƥ�����Ÿ���ʱ��(��λΪ 1/10 s) set ignorecase "��������ʱ����Դ�Сд 
syntax on "�����﷨


let Tlist_Show_One_File=1                                                                                                                 
let Tlist_Exit_OnlyWindow=1                                                                                                                                                  
let g:winManagerWindowLayout='FileExplorer|TagList'                                                                                                                         
nmap wm :WMToggle<cr> 