package JOP2022_08_01;


import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


public class SoupTest {
    
    public String soupWikipedia() throws IOException{
        Mboard a=new Mboard();
        Document doc=null;
        String str="", url="https://www.tnet.org.tw/Member/List/99999?page=2";
        
        for(int i=1; i<=16; i++){
            url="https://www.tnet.org.tw/Member/List/99999?page="+Integer.toString(i);
            doc = Jsoup.connect(url).get();
            Elements bElements=doc.getElementsByClass("row member-list");
            for(Element b:bElements){
                str += a.textMessage(b.getElementsByClass("member-list__title").text());
                str += a.textMessage(b.getElementsByClass("member-list__link").text())+"<br>";
            }
        }
        
        
        
        
        return str;
    }
    
}
