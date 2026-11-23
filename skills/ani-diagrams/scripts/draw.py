"""Create editable standalone SVG and an equivalent static SVG. Standard library only."""
import sys,json,re
from pathlib import Path
from xml.etree import ElementTree as E
NS='http://www.w3.org/2000/svg'; E.register_namespace('',NS)

def build(d,static=False):
    required={'change':{'start','end','insert'},'branch':{'start','routes','selected'},'handoff':{'sender','receiver','object','end_state'}}
    mode=d['mode']; expected={'mode','title','caption'}|required[mode]; assert_fields=set(d)
    if assert_fields!=expected: raise ValueError('Expected fields: '+', '.join(sorted(expected)))
    def txt(s,limit):
        if not isinstance(s,str) or not s.strip() or len(s)>limit or re.search(r'[\x00-\x1f\x7f]',s):raise ValueError(f'Use a short nonempty single line, up to {limit} characters: {s!r}')
        return s.strip()
    title=txt(d['title'],52);caption=txt(d['caption'],90)
    bg,ink,muted,accent,accentink={'change':('#f7f2e8','#302b25','#605c50','#ecd5ad','#503b1d'),'branch':('#142724','#f3f2e6','#b6c5b7','#efc98a','#342a1a'),'handoff':('#f0eef7','#2b2742','#55516a','#564b83','#fff')}[mode]
    root=E.Element('{%s}svg'%NS,{'viewBox':'0 0 880 500','width':'880','height':'500','role':'img','aria-labelledby':'title desc'});
    def el(tag,attrs=None,t=None,parent=None):
        x=E.SubElement(root if parent is None else parent,'{%s}%s'%(NS,tag),{k:str(v) for k,v in (attrs or {}).items()});x.text=t;return x
    el('title',{'id':'title'},title);desc=el('desc',{'id':'desc'},caption)
    css='text{font-family:Arial,sans-serif}.mono{font-family:monospace;letter-spacing:1px}.title{font-family:Georgia,serif;font-style:italic}.fallback{display:none}@media(prefers-reduced-motion:reduce){.moving{display:none}.fallback{display:inline}}';el('style',t=css)
    def text(x,y,t,size=22,anchor='start',cl='',color=None,weight='normal',parent=None):return el('text',{'x':x,'y':y,'font-size':size,'font-weight':weight,'text-anchor':anchor,'class':cl,'fill':color or ink},t,parent)
    def path(v,col,width=2,more=None,parent=None):return el('path',{'d':v,'fill':'none','stroke':col,'stroke-width':width,**(more or {})},parent=parent)
    def rect(x,y,w,h,col,r=0,parent=None):return el('rect',{'x':x,'y':y,'width':w,'height':h,'rx':r,'fill':col},parent=parent)
    def anim(p,tag,**args):return el(tag,{'dur':'5s','fill':'freeze',**args},parent=p)
    rect(0,0,880,500,bg);text(44,54,{'change':'01 / KORREKTUR','branch':'02 / ENTSCHEIDUNGSWEICHE','handoff':'03 / OBJEKTÜBERGABE'}[mode],16,cl='mono',color=muted);text(44,129,title,min(51,round(1070/max(len(title),1))),cl='title');path('M44 422H836',muted,1);text(44,462,caption,min(20,round(1410/max(len(caption),1))))
    if mode=='change':
        a,b,c=txt(d['start'],12),txt(d['end'],12),txt(d['insert'],27);desc.text=f'Bisher: {a} → {b}. Neu: {a} → {c} → {b}. '+caption
        for y,k in ((249,'Bisher'),(351,'Neu')):
            text(44,y-37,k,16,cl='mono',color=muted);text(44,y+7,a,22,weight='bold');text(836,y+7,b,22,'end',weight='bold');path(f'M213 {y}H662l-10 -6m10 6l-10 6',muted)
        rect(275,320,330,62,accent,4);text(440,358,c,22,'middle',color=accentink,weight='bold');
        if not static:
            x=el('rect',{'class':'moving','x':272,'y':317,'width':336,'height':68,'rx':6,'stroke':'#8e612e','fill':'none','stroke-width':3,'pathLength':100,'stroke-dasharray':'100 100','opacity':0});anim(x,'animate',attributeName='stroke-dashoffset',values='100;100;0;0',keyTimes='0;0.15;0.67;1');anim(x,'animate',attributeName='opacity',values='0;1;1;0;0',keyTimes='0;0.15;0.67;0.85;1')
    elif mode=='branch':
        routes=d['routes'];sel=d['selected'];start=txt(d['start'],12)
        if not isinstance(routes,list) or len(routes)!=2 or type(sel)!=int or sel not in (0,1):raise ValueError('branch needs two routes; selected is 0 or 1')
        text(44,277,start,22,weight='bold');path('M210 270H265',muted);rr=[]
        for i,(y,route) in enumerate(zip((208,333),routes)):
            if not isinstance(route,dict) or set(route)!={'when','end'}:raise ValueError('route needs when and end')
            when,end=txt(route['when'],18),txt(route['end'],20);rr.append((when,end));v=f'M265 270 C335 270 345 {y} 408 {y} H570';path(v,muted);text(432,y-13,when,16,'middle',color=muted);text(594,y+7,end,22,color=accent if i==sel else ink,weight='bold');
            if i==sel:
                text(594,y+32,'BEISPIELPFAD',12,cl='mono',color=accent)
                if not static:
                    x=path(v,accent,4,{'class':'moving','pathLength':100,'stroke-dasharray':'100 100'});anim(x,'animate',attributeName='stroke-dashoffset',values='100;100;0;0',keyTimes='0;0.15;0.73;1')
        desc.text=f'{start}: '+ '; '.join(f'{w} → {e}' for w,e in rr)+f'. Beispiel: {rr[sel][0]}. '+caption
    else:
        a,b,o,state=txt(d['sender'],19),txt(d['receiver'],19),txt(d['object'],15),txt(d['end_state'],33);desc.text=f'{a} übergibt {o} an {b}. {state}. '+caption;text(44,240,a,23,weight='bold');text(836,240,b,23,'end',weight='bold');path('M90 307H780l-10 -6m10 6l-10 6',muted);text(836,380,state,17,'end',color=muted)
        def token(parent):rect(44,278,190,56,accent,5,parent);text(139,314,o,21,'middle',color=accentink,weight='bold',parent=parent)
        g=el('g',{'class':'' if static else 'fallback','transform':'translate(602 0)'});token(g)
        if not static:
            g=el('g',{'class':'moving'});anim(g,'animateTransform',attributeName='transform',type='translate',values='0 0;0 0;602 0;602 0',keyTimes='0;0.15;0.65;1');token(g)
    return E.tostring(root,encoding='utf-8',xml_declaration=True)

if __name__=='__main__':
    if len(sys.argv)!=3:sys.exit('Usage: python3 draw.py spec.json NEW_OUTPUT_DIR')
    try:
        data=json.loads(Path(sys.argv[1]).read_text(encoding='utf8')); files={n:build(data,s) for n,s in [('diagram.svg',False),('still.svg',True)]};out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
        for n,v in files.items():(out/n).write_bytes(v)
    except (ValueError,KeyError,TypeError,OSError) as e:sys.exit(str(e))
