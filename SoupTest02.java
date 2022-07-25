package JOP2022_soup_02;


import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


public class SoupTest02 {
    
    public String soupWikipedia() throws IOException{
        Mboard a=new Mboard();
        Document doc_a=null, doc_b=null;
        String str="爬蟲02"+"<br>", url_a="https://www.tnet.org.tw/Member/List/99999?page=2", url_b="";
        int j=1, k=1;
        for(int i=1; i<=16; i++){
            url_a="https://www.tnet.org.tw/Member/List/99999?page="+Integer.toString(i);
            doc_a = Jsoup.connect(url_a).get();
            Elements bElements=doc_a.getElementsByClass("row member-list");
            for(Element b:bElements){
                
                str += Integer.toString(j++)+": ";
                str += a.textMessage(b.getElementsByClass("member-list__title").text());
                str += a.textMessage(b.getElementsByClass("member-list__link").text())+"&nbsp";
                if(a.textMessage(b.getElementsByClass("member-list__link").text()).isEmpty()) {
                    str += "<br>";
                    continue;
                }

                url_b=b.getElementsByClass("member-list__link").text();
                //if(j==7) 
                //    break;
                try{
                    doc_b = Jsoup.connect(url_b).get();
                    str += doc_a.text().contains("能量")?"「有」能量字眼:"+Integer.toString(k++):"沒有能量相關";
                }catch(Exception e){
                    str += "Error: "+e;
                }                
                str += "<br>";
            }
            str +="「有」能量相關的公司共 "+Integer.toString(k++);
        }
        return str;
    }
    
}
